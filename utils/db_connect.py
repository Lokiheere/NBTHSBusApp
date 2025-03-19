import mysql.connector

def get_connection(host, user, password, database, port): 
    return mysql.connector.connect(
        host= host,
        user= user,
        password= password,
        database= database,
        port= port, 
    )