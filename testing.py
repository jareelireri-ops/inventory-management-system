import unittest
from app import app

class InventoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_inventory(self):
        """Test if the inventory returns a 200 status."""
        response = self.app.get('/inventory')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_item(self):
        """Test if a non-existent item returns a 404."""
        response = self.app.get('/inventory/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()