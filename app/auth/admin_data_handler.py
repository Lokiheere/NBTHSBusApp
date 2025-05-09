import mysql
from flask import render_template, request, session, redirect, url_for, flash
from flask_wtf.csrf import validate_csrf
from app.utils.db_connect import get_connection


def login_user():
    """
    Gets the login authentication from mySQL database and checks if they are valid.
    If valid, it redirects to the management page.
    If not valid, pops the session and returns an error message.
    
    Keyword arguments:
    None -- (Relies on request.form for user input of 'name' and 'passcode' in templates/auth/index.html)
    
    Return: 
    - Redirect to '/management/<username>' if authentication are valid.
    - Redirect to auth page if authentication are invalid.
    """

    msg = ''
    with get_connection() as connection:
        try:
            connection.ping(reconnect=True)
        except mysql.connector.Error as e:
            print(f"MySQL Error: {str(e)}")
            connection.rollback()

        with connection.cursor() as cursor:
            try:
                if request.method == 'POST':
                    try:
                        validate_csrf(request.form['csrf_token'])
                    except:
                        flash("CRSF token is invalid or missing, please try again.", "error")
                        return redirect(url_for('authen.auth'))

                    name = request.form['name']
                    passcode = request.form['passcode']
                    cursor.execute("SELECT * FROM users WHERE name = %s AND passcode = %s", (name, passcode))
                    record = cursor.fetchone()

                    if record and name == record[1]:
                        session['loggedin'] = True
                        session['name'] = record[1]
                        username = record[1]
                        return redirect(url_for('management_bp.management', username=username))
                    else:
                        session.pop('loggedin', None)
                        session.pop('name', None)
                        msg = 'Invalid username or password'

            finally:
                cursor.close()
                connection.close()

    return render_template('auth/index.html', msg=msg)


def logout_user():
    """
    This function handles the logout process for the user by popping (removing) 'loggin' and 'name' in the Flask session.
    
    Keyword arguments:
    None -- (Relies on session to pop 'loggedin' and 'name')
    Return:
    - Redirect to authentication page after logout.
    """

    session.pop('loggedin', None)
    session.pop('name', None)
    return redirect(url_for('authen.auth'))
