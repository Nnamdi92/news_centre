# This contains utility functions that will help us interactwith the database

from mysql.connector import Error

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
 
def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)  # Return results as dictionaries
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()  # Fetch all rows for SELECT queries
            return result  # Return the retrieved data
        else:
            connection.commit()  # Commit for INSERT, UPDATE, DELETE
            print("Query executed successfully")
            return None
    except Error as err:
        print(f"Error: '{err}'")
        return None