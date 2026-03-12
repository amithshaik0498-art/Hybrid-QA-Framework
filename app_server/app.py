from flask import Flask, jsonify

app = Flask(__name__)

# This is our mock database for testing
inventory = [
    {"id": 1, "name": "Standard Backpack", "price": 29.99},
    {"id": 2, "name": "Bike Light", "price": 9.99}
]

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

if __name__ == '__main__':
    # This runs the server on your local machine
    app.run(debug=True, port=5000)