import random

import psycopg2
from faker import Faker

import connect_postgres_db as cn


def create_table(cursor):
    try:
        # SQL statement to create tables
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS posts (
                post_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                title VARCHAR(100) NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

        # Execute the create table query
        cursor.execute(create_table_query)
        print("Tables created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while creating tables in PostgreSQL:", error)


def insert_data(cursor, data):
    try:
        # SQL statements to insert data into tables
        insert_query_tb1 = "INSERT INTO users (username, email) VALUES (%s, %s);"
        insert_query_tb2 = (
            "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s);"
        )

        # Execute the insert queries
        cursor.executemany(insert_query_tb1, [(d[0], d[1]) for d in data])
        cursor.executemany(insert_query_tb2, [(d[2], d[3], d[4]) for d in data])

        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL:", error)


def generate_mock_data(num_rows):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        username = fake.user_name()
        email = fake.email()
        title = fake.sentence()
        content = fake.paragraph()
        user_id = random.randint(1, 10000)  # Assuming you have 1000 users
        data.append((username, email, user_id, title, content))
    return data


if __name__ == "__main__":
    # Connect to the database
    connection = cn.connect_to_db()
    cursor = connection.cursor()

    # Create table
    create_table(cursor)

    # Generate mock data
    num_rows = 1000000
    data = generate_mock_data(num_rows)

    # Insert data
    insert_data(cursor, data)

    # Commit and close connection
    connection.commit()
    cursor.close()
    connection.close()
