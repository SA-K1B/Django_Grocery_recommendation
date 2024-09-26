# test_views.py
from django.test import TestCase
from django.urls import reverse
from django.core.files.storage import default_storage
import pickle
import os
from django.conf import settings


class ItemViewsTests(TestCase):

    def setUp(self):
        # Create mock data for testing
        self.mock_top_items = ["apple", "banana", "orange"]
        self.mock_all_items = ["apple", "banana", "orange", "grape", "mango"]
        self.mock_rules = {}  # Replace with actual rule structure if needed

        # Save mock data to pickle files
        with open(
            os.path.join(settings.BASE_DIR, "model", "top_items_test.pkl"), "wb"
        ) as f:
            pickle.dump(self.mock_top_items, f)
        with open(
            os.path.join(settings.BASE_DIR, "model", "all_items_test.pkl"), "wb"
        ) as f:
            pickle.dump(self.mock_all_items, f)
        with open(
            os.path.join(settings.BASE_DIR, "model", "rules_test.pkl"), "wb"
        ) as f:
            pickle.dump(self.mock_rules, f)

    def tearDown(self):
        # Clean up the pickle files after tests
        for filename in ["top_items_test.pkl", "all_items_test.pkl", "rules_test.pkl"]:
            path = os.path.join(settings.BASE_DIR, "model", filename)
            if os.path.exists(path):
                os.remove(path)

    def test_get_num_items_valid_post(self):
        response = self.client.post(reverse("num_items"), {"num_items": 2})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item_input.html")
        self.assertIn("num_items", response.context)
        self.assertIn("top_items", response.context)

    def test_get_num_items_invalid_post(self):
        response = self.client.post(reverse("num_items"), {"num_items": 0})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "num_of_items.html")

    def test_get_items_valid_post(self):
        response = self.client.post(
            reverse("item_input", args=[2]), {"item_1": "soda", "item_2": "chewing gum"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recommend.html")
        self.assertIn("items", response.context)

    def test_get_items_invalid_post(self):
        response = self.client.post(
            reverse("item_input", args=[2]),
            {"item_1": "apple", "item_2": "notarealitem"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notfound.html")
