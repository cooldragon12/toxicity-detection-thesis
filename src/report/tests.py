from django import setup
from django.test import TestCase

setup()


# Create your tests here.
class TestReport(TestCase):
    def test_report_view(self):
        response = self.client.get("/report/add/")
        self.assertEqual(response.status_code, 200)

    def test_report_view_post(self):
        response = self.client.post(
            "/report/add/",
            {
                "email": "johndel@gmail.com",
                "name": "John Dela Cruz",
                "username": "johndel#1234",
                "gender": "male",
                "age": 20,
                "country": "PH",
                "province": "Manila",
                "average_hours": 2,
                "frequency": 2,
                "in_game_rank": "Gold 1",
                "often_server": "Hong Kong",
                "player_entries-TOTAL_FORMS": 1,
                "player_entries-INITIAL_FORMS": 0,
                "player_entries-MIN_NUM_FORMS": 0,
                "player_entries-MAX_NUM_FORMS": 1000,
                "player_entries-0-text": "Hello",
                "player_entries-0-screenshot": "",
                "player_entries-0-description": "Hello",
                "player_entries-0-emotion": "Happy",
                "player_entries-0-toxicity": "Not Toxic",
                "player_entries-0-sentiment": "Positive",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_report_view_post_invalid(self):
        response = self.client.post(
            "/report/add/",
            {
                "email": "johnmda",
                "first_name": "John",
                "last_name": "Del",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "error")
