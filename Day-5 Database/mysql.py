import pymysql

# Function to connect to the MySQL server
def connect_to_server():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Karthi21@2120",
            port=3306
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Connection to server failed: {e}")
        return None

# Function to create the database if it doesn't exist
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

# Function to connect to the specific database
def connect_to_database():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="Karthi21@2120",
            db="office",
            port=3306
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Connection to database failed: {e}")
        return None

# Function to create the games table if it doesn't exist
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

# Function to insert a row into the games table
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

# Function to read and print all game data from the games table
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

# Function to update a row in the games table
def update_row(connection, game_id, name, price, num_players, max_players, description):
    try:
        cursor = connection.cursor()
        update_query = """
        UPDATE games
        SET name = %s, price = %s, num_players = %s, max_players = %s, description = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (name, price, num_players, max_players, description, game_id))
        connection.commit()
        print("Row updated successfully")
    except pymysql.MySQLError as e:
        print(f"Failed to update row: {e}")
    finally:
        cursor.close()

# Function to delete a row from the games table
def delete_row(connection, game_id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM games WHERE id = %s"
        cursor.execute(delete_query, (game_id,))
        connection.commit()
        print("Row deleted successfully")
    except pymysql.MySQLError as e:
        print(f"Failed to delete row: {e}")
    finally:
        cursor.close()

# Function to search for a game by ID
def search_by_id(connection, game_id):
    try:
        cursor = connection.cursor()
        search_query = "SELECT * FROM games WHERE id = %s"
        cursor.execute(search_query, (game_id,))
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print("No game found with the provided ID")
    except pymysql.MySQLError as e:
        print(f"Failed to search for game: {e}")
    finally:
        cursor.close()

def main():
    try:
        # Establish the connection to the server
        server_connection = connect_to_server()
        if server_connection:
            print("Connected to server")

            # Create the database
            create_database(server_connection)

            # Close the server connection
            server_connection.close()
            print("Server connection closed")

        # Establish the connection to the database
        database_connection = connect_to_database()
        if database_connection:
            print("Connected to database")

            # Create the table
            create_table(database_connection)

            while True:
                print("\nMenu:")
                print("1. Insert a new game")
                print("2. Update an existing game")
                print("3. Read game data")
                print("4. Delete a game")
                print("5. Search for a game by ID")
                print("6. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    # Get user input for a new game entry
                    name = input("Enter the game name: ")
                    price = float(input("Enter the game price: "))
                    num_players = int(input("Enter the number of players: "))
                    max_players = int(input("Enter the maximum number of players: "))
                    description = input("Enter the game description: ")

                    # Insert a row into the games table
                    insert_row(database_connection, name, price, num_players, max_players, description)

                elif choice == "2":
                    # Get user input for updating an existing game entry
                    game_id = int(input("Enter the game ID to update: "))
                    new_name = input("Enter the new game name: ")
                    new_price = float(input("Enter the new game price: "))
                    new_num_players = int(input("Enter the new number of players: "))
                    new_max_players = int(input("Enter the new maximum number of players: "))
                    new_description = input("Enter the new game description: ")

                    # Update the row in the games table
                    update_row(database_connection, game_id, new_name, new_price, new_num_players, new_max_players, new_description)

                elif choice == "3":
                    # Read and print game data
                    print("Reading game data:")
                    read_game_data(database_connection)

                elif choice == "4":
                    # Get user input for deleting a game
                    game_id = int(input("Enter the game ID to delete: "))

                    # Delete the row from the games table
                    delete_row(database_connection, game_id)

                elif choice == "5":
                    # Get user input for searching a game by ID
                    game_id = int(input("Enter the game ID to search: "))

                    # Search for the game by ID
                    search_by_id(database_connection, game_id)

                elif choice == "6":
                    # Exit the program
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice. Please try again.")

            # Close the database connection
            database_connection.close()
            print("Database connection closed successfully")

    except pymysql.MySQLError as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()

