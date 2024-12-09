import mysql.connector
from mysql.connector import Error

# SQL query to create the Products table
create_table_query = """
CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
"""

# SQL queries for CRUD operations
insert_product_query = """
INSERT INTO Products (name, price) 
VALUES (%s, %s);
"""

select_all_products_query = "SELECT * FROM Products;"

update_product_query = """
UPDATE Products 
SET name = %s, price = %s 
WHERE id = %s;
"""

delete_product_query = """
DELETE FROM Products WHERE id = %s;
"""

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="1234", 
            database="oxzon"
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table(cursor):
    try:
        cursor.execute(create_table_query)
        print("Products table created successfully")
    except Error as e:
        print(f"Error while creating table: {e}")

def create_product(cursor, name, price):
    try:
        cursor.execute(insert_product_query, (name, price))
        print(f"Product '{name}' inserted successfully")
    except Error as e:
        print(f"Error while inserting product: {e}")

def read_products(cursor):
    try:
        cursor.execute(select_all_products_query)
        products = cursor.fetchall()
        print("Products in the database:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
    except Error as e:
        print(f"Error while reading products: {e}")

def update_product(cursor, product_id, name, price):
    try:
        cursor.execute(update_product_query, (name, price, product_id))
        if cursor.rowcount > 0:
            print(f"Product with ID {product_id} updated successfully")
        else:
            print(f"Product with ID {product_id} not found")
    except Error as e:
        print(f"Error while updating product: {e}")

def delete_product(cursor, product_id):
    try:
        cursor.execute(delete_product_query, (product_id,))
        if cursor.rowcount > 0:
            print(f"Product with ID {product_id} deleted successfully")
        else:
            print(f"Product with ID {product_id} not found")
    except Error as e:
        print(f"Error while deleting product: {e}")

def main():
    # Establish a connection to the database
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        # Create Products table if it doesn't exist
        create_table(cursor)

        # Example CRUD operations
        create_product(cursor, "Laptop", 1200.00)
        create_product(cursor, "Smartphone", 800.50)
        create_product(cursor, "tv", 800.50)
        create_product(cursor, "washing machine", 800.50)

        read_products(cursor)

        # Update a product (change price and name)
        update_product(cursor, 1, "Gaming Laptop", 1500.00)

        read_products(cursor)

        # Delete a product
        delete_product(cursor, 2)

        read_products(cursor)

        # Commit changes
        connection.commit()

    except Error as e:
        print(f"Error during operation: {e}")

    finally:
        # Ensure cursor and connection are closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    main()
