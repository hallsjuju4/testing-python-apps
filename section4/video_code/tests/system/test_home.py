from unittest import TestCase
from app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)
            self.assertEqual(json.loads(r.get_data()), {'message': 'Hello, world!'})
