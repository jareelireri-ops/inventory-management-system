# Inventory Management System

Built this as a backend API for managing store inventory. The idea was simple — a retail company needs to track their products, so I built endpoints to handle all of that plus hooked it up to the OpenFoodFacts API so you can look up a real product by barcode and it gets added to the inventory automatically.

Also built a CLI admin portal so you don't have to use Postman every time you want to interact with the API.

---

## How to run it

First install the dependencies:
```bash
pip install flask requests
```

Then start the API:
```bash
python app.py
```

Open a second terminal and run the admin portal:
```bash
python cli_interface.py
```

To run the tests:
```bash
python testing.py
```

---

## Endpoints

- `GET /inventory` — returns everything in the inventory
- `GET /inventory/<id>` — get one item by its ID
- `POST /inventory` — add a new item
- `PATCH /inventory/<id>` — update price or quantity of an item
- `DELETE /inventory/<id>` — remove an item
- `GET /inventory/lookup/<barcode>` — looks up a product on OpenFoodFacts by barcode and adds it to the inventory

---

## The CLI

The CLI runs against the live API. You get a simple menu where you can view inventory, look up a barcode, update something, or delete an item. Easier than hitting endpoints manually while testing.

---

## What's in the repo

- `app.py` — the Flask app and all the routes
- `external_api.py` — handles the OpenFoodFacts API call
- `cli_interface.py` — the admin CLI
- `testing.py` — unit tests

---

## DEVELOPER

Jareel Ireri — [@jareelireri-ops](https://github.com/jareelireri-ops)
