import mysql.connector

# MySQL configuration for 'apple' database
config = {
    'host': 'localhost',       # Your MySQL server address
    'user': 'your_username',   # Your MySQL username
    'password': 'your_password', # Your MySQL password
    'database': 'apple'        # Existing database name
}

try:
    # Establish the connection to MySQL
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print(f"Successfully connected to the 'apple' database")
        
        # Example of querying data from the 'apple' database
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print(f"Connected to: {result[0]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the connection
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
