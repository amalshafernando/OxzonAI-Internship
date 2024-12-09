import mysql.connector

query = """
CREATE TABLE Products(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL
)
"""
try:
  # Establish a connection to the database
  connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="oxzon")
  print("connected to the database")  #printing the connection object
  cursor = connection.cursor() #creating the cursor object
  cursor.execute(query)
  print("Table created successfully")
except:
  print("connection failed")
finally:
    # Ensure cursor and connection are closed
    if connection.is_connected():
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("Connection closed")


