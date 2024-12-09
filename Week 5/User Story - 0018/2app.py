import mysql.connector

create_table_query = """
CREATE TABLE Products(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL
)
"""
insert_data_query = """
INSERT INTO Products (name, price) values
('Samsung A02', 30000),
('Samsung A12', 40000),
('Samsung A22', 50000),
('Samsung A32', 60000),
('Samsung A52', 70000),
('Apple iphone', 100000)
"""
read_data_query = "SELECT * FROM Products"
update_data_query = "UPDATE Products SET price = %s WHERE id = %s"
delete_data_query = "DELETE FROM Products WHERE id = %s"

try:
  # Establish a connection to the database
  connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="oxzon")
  if connection.is_connected():
    print("Connected to MySQL Database") #printing the connection object
    cursor = connection.cursor() #creating the cursor object
    #cursor.execute(query)
    
    # 1. create a new table
    cursor.execute(create_table_query)
    print("Table created successfully")
    
    # 2. insert data
    cursor.execute(insert_data_query)
    connection.commit
    print("Data inserted successfully")
    
    # 3. retrieve data
    cursor.execute(read_data_query)
    
    # 4. update data
    
    # 5. delete data
    
  
except:
  print("connection failed")
finally:
    # Ensure cursor and connection are closed
    if connection.is_connected():
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("Connection closed")


