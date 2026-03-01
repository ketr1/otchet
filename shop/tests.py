from django.test import TestCase

class PagesTest(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_products_page_status_code(self):
        response = self.client.get("/products/")
        self.assertIn(response.status_code, (200, 302))