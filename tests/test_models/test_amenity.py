#!/usr/bin/python3
"""contains TestCase for amenities.py
    TestClasses:
        test_constructor
        test_initilization
        test_set_values
        test_save_values
"""
import models
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import json

class TestCaseAmenity(unittest.TestCase):
#constructortests
    def test_constructor(self):
        """Test case constructor"""

        amenity = Amenity()

        self.assertEqual(amenity.name, "")

    def test_constructor_with_args(self):
        """unittest for constructor with arguments"""

        amenity = Amenity(name="Steam bath")

        self.assertEqual(amenity.name, "Steam bath")

#functionalitytests
    def test_amenity_equal(self):
        """test that amenity returns correct for two amenities"""

        amenityA = Amenity(name="steam bath")
        amenityB = Amenity(name="Saloon")

        self.assertFalse(amenityA == amenityB)

        amenityB.name = "Balcony"

        self.assertFalse(amenityA == amenityB)

    def test_get_value(self):
        """test to get value"""

        amenity = Amenity(name="Steam shower")

        expected_amenity = {"name": "Steam shower"}
        
        got_amenity = {
                key: getattr(amenity, key) for key in expected_amenity
                }
        
        self.assertEqual(expected_amenity, got_amenity)
#validationtests

    def test_amenity_sublass_BaseModel(self):
        """Test amenity is subclass BaseModel"""

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_name_string(self):
        """test amenity name is string"""

        amenity = Amenity(name="Personal Chauffer")

        self.assertIsInstance(amenity.name, str)
        
    def test_amenity_save_update_delete_to_json(self):
        """test to chek whether amenity oblect has been saved to Json
        retrieved from JSON, Updated, or deleted"""

        amenity = Amenity(name="wifi")

        with open("amenity.json", "w") as f:
            json.dump(amenity.name, f)

        with open("amenity.json", "r") as f:
            json.load(f)

        amenity_object = Amenity(name="amenity short file example")

        amenity.name = "steam shower and chauffer"
        
        #save

        with open("amenity.json", "w") as f:
            json.dump(amenity_object.name, f)

        #delete json file
        os.remove("amenity.json")
#destructortests
    def test_destructor(self):
        """test to check the amenity attribute destroyed"""

        amenity = Amenity()

        del amenity

        with self.assertRaises(NameError):
            amenity.name

if __name__ == "__main__":
    unittest.main()
