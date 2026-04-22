# Inventory Management System

A REST API built with Flask for a small retail company. Employees can manage inventory items through the API or through a CLI admin portal. The system also connects to the OpenFoodFacts API to pull real product data by barcode and add it directly to the inventory.

---

## Setup

**1. Clone the repo and navigate into it**
```bash
git clone <your-repo-link>
cd inventory-management-system
```

**2. Install dependencies**
```bash
pip install flask requests
```

**3. Run the API**
```bash
python app.py
```
Runs at `http://127.0.0.1:5000`

**4. Run the Admin Portal** (in a separate terminal while the API is running)
```bash
python cli_interface.py
```

**5. Run Tests**
```bash
python testing.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/inventory` | Get all inventory items |
| GET | `/inventory/<id>` | Get a single item by ID |
| POST | `/inventory` | Add a new item |
| PATCH | `/inventory/<id>` | Update an item's price or quantity |
| DELETE | `/inventory/<id>` | Delete an item |
| GET | `/inventory/lookup/<barcode>` | Fetch product from OpenFoodFacts and add to inventory |

---

## CLI Admin Portal

The CLI lets you interact with the API without needing Postman or a browser. Options include:

1. View full inventory
2. Lookup a product by barcode (calls OpenFoodFacts and adds it to inventory)
3. Update a product's price or quantity
4. Delete a product
5. Exit

---

## Project Structure

```
inventory-management-system/
├── app.py              # Flask app and all routes
├── external_api.py     # OpenFoodFacts integration
├── cli_interface.py    # CLI admin portal
├── testing.py          # Unit tests
└── README.md
```

---

## Features

- Full CRUD operations on inventory
- Real-time product lookup by barcode via OpenFoodFacts
- Fetched products are automatically added to the inventory array
- CLI interface for admin use without a frontend
- Unit tests covering endpoints and external API integration

---

## developer

Jareel Ireri — [@jareelireri-ops](https://github.com/jareelireri-ops)
