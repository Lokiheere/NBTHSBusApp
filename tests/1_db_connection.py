class DBConnection:
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port,
        }
        
    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)
        
        #Tawsif here this is just to check if the connection is successful or not
        print(f"Successfully connected to the database '{self.config['database']}' at {self.config['host']}:{self.config['port']}")
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An error occurred: {exc_value}")
        self.cursor.close()
        self.connection.close()

