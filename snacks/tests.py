from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnakesTests(TestCase):
    def test_list_page_status_code(self):
        url= reverse('snacks_list')
        actual=self.client.get(url).status_code
        expected=200
        self.assertEqual(actual,expected)
    def test_list_url_template(self):
        url= reverse('snacks_list')
        actual=self.client.get(url)
        expected='snack_list.html'
        self.assertTemplateUsed(actual, expected)

    