import mysql.connector
from mysql.connector import Error

# Query for creating the table
create_table_query = """
CREATE TABLE IF NOT EXISTS Products(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL
)
"""

# Query to insert demo data
insert_data_query = """
INSERT INTO Products (name, price) 
VALUES
  ('Product A', 10.99),
  ('Product B', 20.49),
  ('Product C', 30.99),
  ('Product D', 40.49),
  ('Product E', 50.00)
"""

# Query for CRUD operations
read_data_query = "SELECT * FROM Products"
update_data_query = "UPDATE Products SET price = %s WHERE id = %s"
delete_data_query = "DELETE FROM Products WHERE id = %s"

# Function for performing CRUD operations
def perform_crud_operations():
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="oxzon")
        if connection.is_connected():
            print("Connected to the database")

            cursor = connection.cursor()

            # 1. Create table (if not exists)
            cursor.execute(create_table_query)
            print("Table created successfully (if it didn't exist)")

            # 2. Insert demo data into the table
            cursor.execute(insert_data_query)
            connection.commit()
            print("Demo data inserted successfully")

            # 3. Read data (Retrieve all products)
            cursor.execute(read_data_query)
            result = cursor.fetchall()
            print("Read Data (All products):")
            for row in result:
                print(row)

            # 4. Update data (example: update price for Product with id=1)
            cursor.execute(update_data_query, (99.99, 1))
            connection.commit()
            print("Data updated successfully")

            # Read data again after update to verify
            cursor.execute(read_data_query)
            result = cursor.fetchall()
            print("Read Data after update:")
            for row in result:
                print(row)

            # 5. Delete data (example: delete product with id=3)
            cursor.execute(delete_data_query, (3,))
            connection.commit()
            print("Data deleted successfully")

            # Read data again after delete to verify
            cursor.execute(read_data_query)
            result = cursor.fetchall()
            print("Read Data after delete:")
            for row in result:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Ensure cursor and connection are closed
        if connection.is_connected():
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
            print("Connection closed")

# Execute the CRUD operations
perform_crud_operations()
