from flask import render_template
from . import errors


@errors.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500
