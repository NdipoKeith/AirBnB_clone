#!/usr/bin/python3
"""TestCases for review.py file
    TestCase for initialization
    testcase for constructor
    testcase for destructor
"""
import models
import unittest
from models.review import Review
from models.base_model import BaseModel
import json
import os

class TestCaseReviw(unittest.TestCase):
#constructor tests
    def test_constructor(self):
        """ensures the constructor correctly initialized with kwargs"""

        review = Review()

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_constructor_with_arguments(self):
        """Testcase to check output correct as input review args"""

        review = Review(place_id="39", user_id="49", text="Great customer service in general")

        self.assertEqual(review.place_id, "39")
        self.assertEqual(review.user_id, "49")
        self.assertEqual(review.text, "Great customer service in general")

#setters and getters tests
    def test_get_value(self):
        """test to check value taken is correct"""

        review = Review(place_id="39", user_id="459", text="Okay")

        review.place_id = "499"
        self.assertEqual(review.place_id, "499")

        review.user_id = "30"
        self.assertEqual(review.user_id, "30")

        review.text = "changed my mind, poor customer service"
        updated_review = review.text

        self.assertEqual(review.text, updated_review)


    def test_place_id_string(self):
        """test to check place_id string"""

        review = Review(place_id="456")

        self.assertIsInstance(review.place_id, str)

    def test_user_id_str(self):
        """test to check user_id string"""

        review = Review(user_id="039")

        self.assertIsInstance(review.user_id, str)

    def test_text_str(self):
        """test to check if test string"""

        review = Review(text="Good accomodation")

        self.assertIsInstance(review.text, str)

    def test_review_subclass_BaseModel(self):
        """test if review subclass of BaseModel"""

        self.assertTrue(issubclass(Review, BaseModel))

    def test_saved_updated_delete_retrieve(self):
        """test to check whether CRUD saved to json"""

        review = Review(place_id="+254", user_id="39", text="Good accomodation")
        
        with open("review.json", "w") as f:
            json.dump(review.place_id, f)
            json.dump(review.user_id, f)
            json.dump(review.text, f)

        with open("review.json", "r") as f:
            review_json = json.load

        review_json_file = review

        review_json_file.user_id = "40"

        with open("review.json", "w") as f:
            json.dump(review_json_file.user_id, f)

        os.remove("review.json")

#destructor tests
    def test_destructor(self):
        """unittest to check whether it destroys the class"""

        review = Review()
        
        del review

        with self.assertRaises(NameError):
            review.place_id
        with self.assertRaises(NameError):
            review.user_id
        with self.assertRaises(NameError):
            review.text

if __name__ == "__main__":
    unittest.main()
