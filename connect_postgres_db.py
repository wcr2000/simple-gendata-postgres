import psycopg2

# Replace these values with your actual database connection details
dbname = "test"
user = "postgres"
password = "root"
host = "localhost"  # Usually 'localhost' if the database is hosted locally
port = "5432"  # Usually '5432' for PostgreSQL

try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Execute a sample query to test the connection
    cursor.execute("SELECT version();")

    # Fetch the result
    db_version = cursor.fetchone()
    print("Connected to the PostgreSQL database. Server version:", db_version)

    # Don't forget to close the cursor and connection when done
    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)
