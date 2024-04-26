"""This module retrieves book data from an external rest api"""
import requests

def get_book_data(api_url):
    """Get book data from external api"""
    response = requests.get(api_url)
    book = response.json()

    book_id = book['id']
    book_title= book['title']
    author= book['author']
    publication_year= book['publication_year']
    return book_id, book_title, author, publication_year
