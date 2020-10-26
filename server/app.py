import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

# Data
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# Helper functions
def remove_book(book_id):
    for book in BOOKS:
        if 'id' in book and book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS (Cross Origin Resource Sharing) 
# on all routes, from any domain, protocol or port (normally only domain where webFE is host)
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    try:
        if request.method == 'POST':
            # POST: Add a new book
            post_data = request.get_json()
            BOOKS.append({
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book added!'
        else:
            # GET: Return all books
            response_object['books'] = BOOKS
    except Exception as e:
        response_object['status'] = 'failure'
        response_object['message'] = "Oops! {} occured.".format(e.__class__)
    # Return the response as JSON
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        # PUT: Update an existing book
        post_data = request.get_json()
        if remove_book(book_id):
            BOOKS.append({
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read')
            })
            response_object['message'] = 'Book updated!'
        else:
            response_object['status'] = 'failure'
            response_object['message'] = 'Wrong id!'
            print(response_object)
    elif request.method == 'DELETE':
        # DELETE: Remove an existing book
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


# Run the flask app
if __name__ == '__main__':
    app.run()