"""the main module to run and get info about the stored book from api"""

from api_data_retr import get_book_data
from data_store import (
    connect_to_database,
    create_table,
    insert_data,
    retrieve_data,
    close_connection,
)

if __name__ == "__main__":
    # coonect to the database
    conn = connect_to_database("book_store.db")

    create_table(conn)

    # fetch the book data from external api
    api_url = "https://freetestapi.com/api/v1/books/1"  # dummy url picked from internet
    id, book_title, author, publication_year = get_book_data(api_url)

    # store the book data in the database
    insert_data(conn, "Books", (id, book_title, author, publication_year))

    # retrieve the book data from the database
    rows = retrieve_data(conn, "Books")
    for row in rows:
        print(row)

    #close the database
    close_connection(conn)
