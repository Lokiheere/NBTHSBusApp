from app.utils.db_connect import get_connection

def initialize_database():
    """
    Initializes the database by creating necessary tables.

    This function establishes a connection to the MySQL database and ensures 
    that the tables 'buses', 'parking_spots', and 'users' exist. If the tables 
    do not exist, they are created with predefined columns to store bus assignments, 
    parking spot occupancy, and user credentials.

    Keyword arguments:
    None -- (Uses database credentials retrieved via get_connection())

    Returns:
    None -- Commits changes and prints confirmation.
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS assigned_buses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    bus_name VARCHAR(255) NOT NULL UNIQUE,
                    spot_name VARCHAR(255) NOT NULL UNIQUE,
                    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS buses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    bus_name VARCHAR(255) NOT NULL UNIQUE,
                    assigned_spot VARCHAR(255) DEFAULT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS parking_spots (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    spot_name VARCHAR(255) NOT NULL UNIQUE,
                    occupied_by VARCHAR(255) DEFAULT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    passcode VARCHAR(255) NOT NULL
                )
            """)
            connection.commit()
            
    print("Database initialized successfully.")