from flask import Flask, jsonify, request

from external_api import fetch_product_by_barcode 

app = Flask(__name__)

# THE DATA T0 WORKING WITH
inventory = [
    {"id": 1, "name": "Passion Fruit", "quantity": 80, "price": 1.49, "barcode": "1234567890"},
    {"id": 2, "name": "Milk", "quantity": 60, "price": 0.89, "barcode": "0987654321"}
]

# the Helper function to find item by ID 
def find_item(item_id):
    """Find an inventory item by ID."""
    return next((item for item in inventory if item["id"] == item_id), None)

# THE ROUTES

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Inventory Management System!"})

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Return all inventory items."""
    return jsonify(inventory), 200

#the EXTERNAL API ROUTE FOR "EXCELLED" STATUS
@app.route('/inventory/lookup/<barcode>', methods=['GET'])
def lookup_and_add(barcode):
    """Fetch product from OpenFoodFacts and add it to the inventory array."""
    
    #Fetch data using our external script
    product_data = fetch_product_by_barcode(barcode)
    
    if not product_data:
        return jsonify({"error": "Product not found in OpenFoodFacts"}), 404
        
    for item in inventory:
        if item['barcode'] == barcode:
            return jsonify({"message": "Item already in inventory", "item": item}), 200

    # Add new item to array
    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "name": product_data["name"],
        "quantity": 0,  
        "price": 0.0,   
        "barcode": barcode
    }
    inventory.append(new_item)
    return jsonify({"message": "Successfully fetched and added", "item": new_item}), 201

@app.route('/inventory/<int:id>', methods=['GET'])
def get_item(id):
    """Return a single item by ID."""
    item = find_item(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

@app.route('/inventory', methods=['POST'])
def create_item():
    """Add a new inventory item."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "name": data["name"],
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0),
        "barcode": data.get("barcode", "")
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:id>', methods=['PATCH'])
def update_item(id):
    """Update an existing inventory item."""
    item = find_item(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    for field in ["name", "quantity", "price", "barcode"]:
        if field in data:
            item[field] = data[field]

    return jsonify(item), 200

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_item(id):
    """Delete an inventory item."""
    global inventory
    item = find_item(id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory = [i for i in inventory if i["id"] != id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
