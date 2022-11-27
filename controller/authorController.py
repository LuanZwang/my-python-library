from flask import request

from ..main import main

@main.route("/api/books", methods=['GET'])
def books():
    return [
        {
            'method': request.method,
            "title": "book_1" }
    ]