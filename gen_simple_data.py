import psycopg2

import connect_postgres_db as cn


def insert_data(connection):
    if connection is not None:
        try:
            # Create a cursor object using the connection
            cursor = connection.cursor()

            # Sample data to insert
            data_to_insert = ("John", "Doe", 30)

            # SQL statement to insert data into a table
            insert_query = "INSERT INTO your_table_name (first_name, last_name, age) VALUES (%s, %s, %s)"

            # Execute the insert query
            cursor.execute(insert_query, data_to_insert)

            # Commit the transaction
            connection.commit()

            print("Data inserted successfully!")

            # Close the cursor
            cursor.close()

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into PostgreSQL:", error)

        finally:
            # Close the connection
            connection.close()
    else:
        print("No connection to the database.")


if __name__ == "__main__":
    # Connect to the database
    connection = cn.connect_to_db()

    # Insert data
    insert_data(connection)
