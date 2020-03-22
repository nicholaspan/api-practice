import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] =  True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# Route that exposes the catalog of books and metadata.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# Route that allows user to select specific book by ID.
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID was provided, assign it to a variable.
    # If no ID is provided, return error message.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id in request. Please provide an ID."

    # Create an empty list for the data returned. 
    results = []

    # Loop though the books list to find matching IDs    
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function to return results as JSON
    return jsonify(results)
    
app.run()
