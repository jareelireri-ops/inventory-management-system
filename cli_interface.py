import requests

# The URL where your Flask app is running
BASE_URL = "http://127.0.0.1:5000/inventory"

def main_menu():
    print("\n=== Inventory Admin Portal ===")
    print("1. View Full Inventory")
    print("2. Lookup Product by Barcode (External API)")
    print("3. Update Product Price/Quantity")
    print("4. Delete Product")
    print("5. Exit")

def run_cli():
    while True:
        main_menu()
        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            # GET /inventory
            try:
                response = requests.get(BASE_URL)
                print("\n--- Current Inventory ---")
                print(response.json())
            except Exception as e:
                print(f"Error connecting to API: {e}")

        elif choice == "2":
            # GET /inventory/lookup/<barcode>
            barcode = input("Enter the product barcode (e.g., 7622300744656): ")
            response = requests.get(f"{BASE_URL}/lookup/{barcode}")
            print(response.json())

        elif choice == "3":
            # PATCH /inventory/<id>
            item_id = input("Enter Item ID to update: ")
            qty = input("New Quantity (leave blank to skip): ")
            price = input("New Price (leave blank to skip): ")
            
            data = {}
            if qty: data["quantity"] = int(qty)
            if price: data["price"] = float(price)
            
            response = requests.patch(f"{BASE_URL}/{item_id}", json=data)
            print(response.json())

        elif choice == "4":
            # DELETE /inventory/<id>
            item_id = input("Enter Item ID to delete: ")
            response = requests.delete(f"{BASE_URL}/{item_id}")
            print(response.json())

        elif choice == "5":
            print("Exiting Admin Portal.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    run_cli()