from django.test import TestCase

# Create your tests here.
from .models import SeasonalFlavour

class SeasonalFlavourTest(TestCase):
    def test_create_flavor(self):
        flavor =SeasonalFlavour.objects.create(
            name="Chocolate Mint",
            about="A refreshing mint chocolate flavor",
            is_available=True,
            start_date="2024-11-01",
            end_date="2024-12-01"
        )