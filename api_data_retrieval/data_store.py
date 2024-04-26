"""This module for the data management in local sql database"""

import sqlite3


# Connect to SQLite database
def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn


# Create a table
def create_table(conn):
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER
            )"""
    )
    conn.commit()
    cur.close()


# Insert data into the table
def insert_data(conn, table_name, data):
    cur = conn.cursor()
    placeholders = ", ".join(["?" for _ in data])
    cur.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
    conn.commit()
    cur.close()


# Retrieve data from the table
def retrieve_data(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    cur.close()
    return rows


# Delete data from the table
def delete_data(conn, table_name, condition):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
    conn.commit()
    cur.close()


# Close the connection
def close_connection(conn):
    conn.close()
