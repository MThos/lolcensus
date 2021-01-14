from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_champion_index_loads(self):
        response = self.client.get('http://127.0.0.1:8000/champion/')
        self.assertEqual(response.status_code, 200)

    def test_item_index_loads(self):
        response = self.client.get('http://127.0.0.1:8000/item/')
        self.assertEqual(response.status_code, 200)