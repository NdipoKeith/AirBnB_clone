#!/usr/bin/python3
"""unittests for city.py
    TesClasses:
        test_constructor correct initializing
        test_constructor with arguments
        test _destructor
"""

import models
import unittest
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.city import City
import json

class TestCaseCity(unittest.TestCase):
#constructortests
    def test_constructor(self):
        """Test case that constructor correctly initializes"""

        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_constructor_with_arguments(self):
        """unit Testcases to check if city is initialized correctly with state_id and name"""

        city = City(state_id="+254", name="Mombasa")

        self.assertEqual(city.state_id, "+254")
        self.assertEqual(city.name, "Mombasa")
#functionaitytests
    def test_city_stateid_different(self):
        """unit TestCase to check city state_id"""

        cityA = City(state_id="+254", name="Mombasa")
        cityB = City(state_id="+254", name="Nairobi")

        self.assertFalse(cityA == cityB)

    def test_state_id_changed(self):
        """unit TestCase for state_id changed it produces an error"""
        
        cityA = City(state_id="+255", name="Dodoma")
        cityB = City(state_id="+255", name="Dodoma")
 
        with self.assertRaises(ValueError):
            raise ValueError("The state_id is not for the city entered above")
        
#getter and setter tests
    def test_get_city_values(self):
        """unit TestCase the get value is correct and is dictionary"""

        city = City(state_id="+254", name="Kisumu")

        expected_output = {'state_id': '+254', 'name': 'Kisumu'}

    def test_city_not_equal_or_otherwise(self):
        """unit TestCase to check if city is same or otherwise"""

        cityA = City(state_id='+254', name='Nairobi')
        cityB = City(state_id='+254', name='Nairobi')

        self.assertFalse(cityA == cityB)

        cityA.name = "Dodoma"

        self.assertFalse(cityA == cityB)

#validation tests
    def test_state_id_string(self):
        """tests to check state_id string"""

        city = City(state_id="+254")

        self.assertIsInstance(city.state_id, str)

    def test_name_string(self):
        """test to check name is string"""

        city = City(name="Nairobi")

        self.assertIsInstance(city.name, str)

    def test_city_sublass_BaseModel(self):
        """tests to check whether city is subclass of basemodel"""

        self.assertTrue(issubclass(City, BaseModel))

    def test_saved_to_json_retrieved_updated_deleed(self):
        """test ro check whether its saved to json, deleted, updated"""

        city = City(state_id="+254", name="Nairobi")

        with open("city.json", "w") as f:
            json.dump(city.name, f)
            json.dump(city.state_id, f)

        #retrieve
        with open("city.json", "r") as f:
            city_json = json.load

        updated_json = city

        updated_json.name = "Dodoma"
        updated_json.state_id = "+255"

        with open("city.json", "w") as f:
            json.dump(updated_json.name, f)
            json.dump(updated_json.state_id, f)

        os.remove("city.json")

        self.assertEqual(city.name, updated_json.name)
        self.assertEqual(city.state_id, updated_json.state_id)


#destructortests
    def test_destructor_for_the_class(self):
        """unit TestCase to check if it's destroyed appropriately"""

        city = City()

        del city

        """check and make sure that the object is not present anymore in the class"""

        with self.assertRaises(NameError):
            city.state_id

        with self.assertRaises(NameError):
            city.name

if __name__ == "__main__":
    unittest.main()
