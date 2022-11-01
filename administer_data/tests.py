from django.test import TestCase

from .savedata import save_data

# Create your tests here.
class ScrapingTest(TestCase):
    def test_save_data(self):
        save_data()


