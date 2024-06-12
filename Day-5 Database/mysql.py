import pymysql

def connect_to_server():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Karthi21@2120",
        port=3306
    )
    return conn
 
def create_database(connection):
    try:
        cursor = connection.cursor()
        create_db_query = "CREATE DATABASE IF NOT EXISTS office"
        cursor.execute(create_db_query)
        print("Database created successfully")
    except pymysql.MySQLError as e:
        print(f"Failed to create database: {e}")
    finally:
        cursor.close()

def connect_to_database():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Karthi21@2120",
        db="office",
        port=3306
    )
    return conn

def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS games (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            num_players INT NOT NULL,
            max_players INT NOT NULL,
            description TEXT
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except pymysql.MySQLError as e:
        print(f"Failed to create table: {e}")
    finally:
        cursor.close()

def insert_row(connection, name, price, num_players, max_players, description):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO games (name, price, num_players, max_players, description)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, price, num_players, max_players, description))
        connection.commit()
        print("Row inserted successfully")
    except pymysql.MySQLError as e:
        print(f"Failed to insert row: {e}")
    finally:
        cursor.close()

def read_game_data(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM games"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except pymysql.MySQLError as e:
        print(f"Failed to read data: {e}")
    finally:
        cursor.close()

try:
    # Establish the connection to the server
    server_connection = connect_to_server()
    print("Connected to server")

    # Create the database
    create_database(server_connection)

    # Close the server connection
    server_connection.close()
    print("Server connection closed")

    # Establish the connection to the database
    database_connection = connect_to_database()
    print("Connected to database")

    # Create the table
    create_table(database_connection)

    # Get user input for a new game entry
    name = input("Enter the game name: ")
    price = float(input("Enter the game price: "))
    num_players = int(input("Enter the number of players: "))
    max_players = int(input("Enter the maximum number of players: "))
    description = input("Enter the game description: ")

    # Insert a row into the games table
    insert_row(database_connection, name, price, num_players, max_players, description)

    # Read and print game data
    print("Reading game data:")
    read_game_data(database_connection)

    # Close the database connection
    database_connection.close()
    print("Database connection closed successfully")

except pymysql.MySQLError as e:
    print(f"Connection failed: {e}")
