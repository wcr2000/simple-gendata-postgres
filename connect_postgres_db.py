import psycopg2


def connect_to_db():
    try:
        # Replace these values with your actual database connection details
        dbname = "test"
        user = "postgres"
        password = "root"
        host = "localhost"  # Usually 'localhost' if the database is hosted locally
        port = "5432"  # Usually '5432' for PostgreSQL

        # Establish a connection to the database
        connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )

        return connection

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None
