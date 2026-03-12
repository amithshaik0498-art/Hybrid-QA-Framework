from flask import Flask, jsonify, request, render_template_string # Added render_template_string here

app = Flask(__name__)

inventory = [
    {"id": 1, "name": "Standard Backpack", "price": 29.99}
]

# 1. API GET Route
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

# 2. API POST Route
@app.route('/api/inventory', methods=['POST'])
def add_item():
    new_item = request.json
    inventory.append(new_item)
    return jsonify(new_item), 201

# 3. UI Route (Moved ABOVE the run block)
@app.route('/inventory-web')
def inventory_ui():
    html = """
    <html>
        <head><title>Inventory Management</title></head>
        <body>
            <h1>Current Stock</h1>
            <ul id="item-list">
                {% for item in items %}
                <li class="inventory-item">{{ item.name }} - ${{ item.price }}</li>
                {% endfor %}
            </ul>
        </body>
    </html>
    """
    return render_template_string(html, items=inventory)

# 4. START THE SERVER (Must be the last thing in the file)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
# --- API DELETE Route ---
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    # Keep everything EXCEPT the item with the matching ID
    inventory = [item for item in inventory if item['id'] != item_id]
    return jsonify({"message": f"Item {item_id} deleted successfully"}), 200