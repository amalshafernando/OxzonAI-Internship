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

# Query to insert product data
insert_data_query = "INSERT INTO Products (name, price) VALUES (%s, %s)"

# Function to perform CRUD operations and add user input
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

            # 2. Insert demo data or user input
            user_input = input("Would you like to add a new product? (yes/no): ").strip().lower()

            if user_input == 'yes':
                # Get user input for product details
                product_name = input("Enter product name: ")
                product_price = float(input("Enter product price: "))

                # Insert data
                cursor.execute(insert_data_query, (product_name, product_price))
                connection.commit()
                print(f"Product '{product_name}' with price {product_price} added successfully!")

            # 3. Read data (Retrieve all products)
            cursor.execute("SELECT * FROM Products")
            result = cursor.fetchall()
            print("All Products in the database:")
            for row in result:
                print(row)

            # 4. Update data (example: update price for Product with id=1)
            cursor.execute("UPDATE Products SET price = %s WHERE id = %s", (99.99, 1))
            connection.commit()
            print("Product price updated successfully.")

            # 5. Delete data (example: delete product with id=3)
            cursor.execute("DELETE FROM Products WHERE id = %s", (3,))
            connection.commit()
            print("Product deleted successfully.")

            # Read data again after update and delete to verify
            cursor.execute("SELECT * FROM Products")
            result = cursor.fetchall()
            print("Updated Products in the database:")
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

# Execute the CRUD operations with user input
perform_crud_operations()
