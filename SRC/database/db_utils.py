from mysql.connector import Error
 
 
def create_database(connection, query):
    """Creates a database using the given query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
 
 
def execute_query(connection, query):
    """Executes a given query. Returns results for SELECT queries, otherwise commits changes."""
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
 
 
def fetch_one(connection, query):
    """Fetches a single record from the database."""
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        result = cursor.fetchone()  # Fetch only one row
        return result  # Returns the first row as a dictionary or None if no data
    except Error as err:
        print(f"Error: '{err}'")
        return None
    
    
    
def drop_database(connection, db_name):
    """Drops the specified database if it exists."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
        print(f"Database '{db_name}' deleted successfully.")
    except Error as err:
        print(f"Error: '{err}'")