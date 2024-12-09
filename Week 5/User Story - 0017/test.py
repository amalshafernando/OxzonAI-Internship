import pyodbc

DRIVER_NAME = 'ODBC Driver 17 for SQL Server'  # Or 'ODBC Driver 18 for SQL Server'
SERVER_NAME = 'SQL2022'  # Or 'localhost\SQL2022' or your actual server name
DATABASE_NAME = 'OxzonAi-2'
USERNAME = 'Amalsha'
PASSWORD = '1234'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={USERNAME};PWD={PASSWORD}'

try:
    conn = pyodbc.connect(connectionString)
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
    

#print(pyodbc.drivers())  # This will list all available drivers    
