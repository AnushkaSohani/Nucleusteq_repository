import mysql.connector

def create_table(cursor):
    try:
        # Define the table schema
        table_schema = (
            "CREATE TABLE IF NOT EXISTS users ("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "username VARCHAR(50) NOT NULL,"
            "email VARCHAR(100) NOT NULL"
            ")"
        )
        
        # Create the table
        cursor.execute(table_schema)
        print("Table 'users' created successfully.")
    except mysql.connector.Error as error:
        print("Error creating table:", error)

def insert_data(cursor, username, email):
    try:
        # Insert data into the table
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        user_data = (username, email)
        cursor.execute(insert_query, user_data)
        print("Data inserted successfully.")
    except mysql.connector.Error as error:
        print("Error inserting data:", error)

def fetch_data(cursor):
    try:
        # Fetch data from the table
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        users = cursor.fetchall()
        
        print("\nUsers:")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    except mysql.connector.Error as error:
        print("Error fetching data:", error)

try:
    # Connect to the database
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    if connection.is_connected():
        print("Connected to MySQL database")
    
    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Create table
    create_table(cursor)

    # Insert data
    insert_data(cursor, "john_doe", "john@example.com")
    insert_data(cursor, "jane_doe", "jane@example.com")

    # Fetch data
    fetch_data(cursor)

except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        # Close cursor and connection
        cursor.close()
        connection.close()
        print("MySQL connection closed")
