import requests

def fetch_product_by_barcode(barcode):
    """Fetch product details from OpenFoodFacts API using a barcode."""
    
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    
    # Required headers to identify the application making the request
    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (student@example.com)"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            return None
        
        data = response.json()
        
        # OpenFoodFacts returns a status of 1 if the product is found, otherwise 0
        if data.get("status") != 1:
            return None
        
        product = data["product"]
        
        # Extract the name and other details, providing fallbacks if necessary
        return {
            "name": product.get("product_name_en") or product.get("product_name", "Unknown Product"),
            "barcode": barcode,
            "quantity": 0,
            "price": 0.0
        }
    except Exception as e:
        print(f"Connection error: {e}")
        return None

if __name__ == "__main__":
    # Testing with Oreo Cookies
    result = fetch_product_by_barcode("7622300744656")
    print(result)