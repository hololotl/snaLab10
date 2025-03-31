import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Dockerized World!', response.data)

if name == '__main__':
    unittest.main()
