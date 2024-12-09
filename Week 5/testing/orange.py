import mysql.connector

# MySQL configuration for 'phones' database
config = {
    'host': 'localhost',        # Your MySQL server address
    'user': 'your_username',    # Your MySQL username
    'password': 'your_password' # Your MySQL password
}

try:
    # Establish the connection (without specifying a database initially)
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Successfully connected to MySQL server.")
        
        # Switch to the 'phones' database
        connection.database = 'phones'

        # Create the 'samsung_models' table
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS samsung_models (
                id INT AUTO_INCREMENT PRIMARY KEY,
                model_name VARCHAR(255) NOT NULL,
                release_year INT NOT NULL
            );
        """)
        print("Table 'samsung_models' created or already exists.")

        # Insert Samsung models into the 'samsung_models' table
        samsung_models = [
            ('Galaxy S23', 2023),
            ('Galaxy S22', 2022),
            ('Galaxy Note 20', 2020),
            ('Galaxy S21', 2021),
            ('Galaxy Z Fold 5', 2023)
        ]
        
        cursor.executemany("INSERT INTO samsung_models (model_name, release_year) VALUES (%s, %s);", samsung_models)
        connection.commit()
        print("Samsung models added to the 'samsung_models' table.")
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Closing the connection
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
