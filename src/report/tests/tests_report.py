import os
from collections.abc import Callable
from io import BytesIO
from typing import Any

from django import test
from PIL import Image
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITransactionTestCase

from ..models import Entry, PlayerDemography

# Create your tests here.


# Create your tests here.
class TestAPIReport(APITransactionTestCase):
    """Test module for Report API"""

    def generate_image_file(self):
        # Generate a test image file
        image = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
        file = BytesIO()
        image.save(file, "png")
        file.name = "test_image.png"
        file.seek(0)
        return file

    def setUp(self):
        # Create test data
        self.player = PlayerDemography.objects.create(
            email="test@example.com",
            name="John Doe",
            gender="Male",
            age=25,
            country="Philippines",
            province="Cavite",
            username="johndoe",
            average_hours=2,
            frequency=5,
            in_game_rank="Gold",
            in_game_rank_level=3,
            often_server="Hong Kong",
        )
        self.entry = Entry.objects.create(
            player_id=self.player,
            text="Test entry",
            description="Test description",
        )

    def tearDown(self):
        # Delete the uploaded image after the test
        if self.entry.screenshot:
            path = self.entry.screenshot.path
            os.remove(path)

    def test_create_player_demography(self):
        """Ensure we can create a new player demography object. with their entry"""
        url = reverse("report")  # Replace "playerdemography-list" with the actual URL name
        data = {
            "email": "newuser@example.com",
            "name": "Jane Smith",
            "gender": "Female",
            "age": 30,
            "country": "Philippines",
            "province": "Cavite",
            "username": "janesmith#8289",
            "average_hours": 3,
            "frequency": 4,
            "in_game_rank": "Silver",
            "in_game_rank_level": 2,
            "often_server": "Hong Kong",
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(PlayerDemography.objects.count(), 2)

    def test_create_entry_using_text(self):
        """Ensure we can create a new entry. with text"""
        url = reverse("add-entry")  # Replace "entry-list" with the actual URL name
        data = {"player_id": self.player.pk, "text": "New entry", "description": "New description"}
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(Entry.objects.count(), 2)

    def test_create_entry_using_screenshot(self):
        """Ensure we can create a new entry. with screenshot"""
        url = reverse("add-entry")
        form_data = {"player_id": self.player.pk, "screenshot": self.generate_image_file()}
        response = self.client.post(url, form_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(Entry.objects.count(), 2)
        path = Entry.objects.filter(player_id=self.player.pk)[1].screenshot.path
        os.remove(path)

    def test_create_entry_using_both(self):
        """Ensure we can create a new entry. with text and screenshot"""
        url = reverse("add-entry")
        form_data = {
            "player_id": self.player.pk,
            "text": "New entry",
            "description": "New description",
            "screenshot": self.generate_image_file(),
        }
        response = self.client.post(url, form_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        self.assertEqual(Entry.objects.count(), 2)
        path = Entry.objects.filter(player_id=self.player.pk)[1].screenshot.path
        os.remove(path)

    def test_get_report(self):
        """Ensure we can get the report"""
        url = reverse("report")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())


class TestReportProcessing(APITransactionTestCase):
    """Test module for Report Processing"""

    def setUp(self):
        # Create test data
        self.player = PlayerDemography.objects.create(
            email="test@example.com",
            name="John Doe",
            gender="Male",
            age=25,
            country="Philippines",
            province="Cavite",
            username="johndoe",
            average_hours=2,
            frequency=5,
            in_game_rank="Gold",
            in_game_rank_level=3,
            often_server="Hong Kong",
        )
        self.entry = Entry.objects.create(
            player_id=self.player,
            text="Test entry",
            description="Test description",
        )

    def generate_image_file(self):
        # Generate a test image file
        image = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
        file = BytesIO()
        image.save(file, "png")
        file.name = "test_image.png"
        file.seek(0)
        return file

    def get_image_file(self):
        # Get existing image file
        image = Image.open("assets_test/test.png")
        file = BytesIO()
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_create_entry_using_both(self):
        """Ensure we can create a new entry. with text and screenshot"""
        url = reverse("add-entry")
        form_data = {
            "player_id": self.player.pk,
            "text": "New entry",
            "description": "New description",
            "screenshot": self.generate_image_file(),
        }
        response = self.client.post(url, form_data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())
        entry = Entry.objects.get(player_id=self.player.pk, text="New entry")
        loc = "chat_screenshots"
        path = entry.screenshot.path
        self.assertEqual(entry.screenshot.name, f"{loc}/{entry.id}_{entry.player_id.pk}.png")
        self.assertEqual(Entry.objects.count(), 2)
        if path:
            os.remove(path)
