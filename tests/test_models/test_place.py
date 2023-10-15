#!/usr/bin/python3
"""TestCase for class Place
    Test functions:
        city_id
        user_id
        name
        number_rooms
        number_bathrooms
        max_guests
        price_by_night
        latitude
        longitude
        amenity_ids
"""
import unittest
import models
from models.place import Place
from models.base_model import BaseModel

class TestCasePlace(unittest.TestCase):
#constructortests
    def test_constructor(self):
        """unittest to check constrictor initialized correctly"""

        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0.0)
        self.assertEqual(place.number_bathrooms, 0.0)
        self.assertEqual(place.max_guest, 0.0)
        self.assertEqual(place.price_by_night, 0.0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
#settertests
    def test_constructor_with_kwargs(self):
        """unittest for constructor with kwargs"""

        place = Place(
                city_id="254",
                user_id="39",
                name="Britam Towers",
                description="Comfy and away from noise",
                number_rooms=6,
                number_bathrooms=7,
                max_guest=7,
                price_by_night=1000,
                latitude=107.11,
                longitude=-99.9,
                amenity_ids=["1", "2"]
               ) 

        self.assertEqual(place.city_id, "254")
        self.assertEqual(place.user_id, "39")
        self.assertEqual(place.name, "Britam Towers")
        self.assertEqual(place.description, "Comfy and away from noise")
        self.assertEqual(place.number_rooms, 6)
        self.assertEqual(place.number_bathrooms, 7)
        self.assertEqual(place.max_guest, 7)
        self.assertEqual(place.price_by_night, 1000)
        self.assertEqual(place.latitude, 107.11)
        self.assertEqual(place.longitude, -99.9)
        self.assertEqual(place.amenity_ids, ["1", "2"])

    def test_set_city(self):
        """Test set_city_id() sets city_id attribute"""

        place = Place()

        place.city_id = "001"

        self.assertEqual(place.city_id, "001")

    def test_set_number_bathrooms(self):
        """Test to check the number of bathroms is set"""

        place = Place()

        place.number_bathrooms = 5

        self.assertEqual(place.number_bathrooms, 5)

#validation tests
    def test_city_id_string(self):
        """test to check city_id returned is string"""
        
        place = Place(city_id="256")

        self.assertIsInstance(place.city_id, str)

    def test_user_id_strinf(self):
        """Test to check user_id string"""

        place = Place(user_id="39")

        self.assertIsInstance(place.user_id, str)

    def test_name_string(self):
        """test to check name string"""

        place = Place("Kempinski Villarosa")

        self.assertIsInstance(place.name, str)

    def test_description_string(self):
        """testcase for desc is string"""

        place = Place("in serene environment")

        self.assertIsInstance(place.description, str)

    def test_number_rooms_int(self):
        """testcase for number of rooms int"""

        place = Place(number_rooms=6)

        self.assertIsInstance(place.number_rooms,int)

    def test_number_bathroom_int(self):
        """test number bathroom is int"""

        place = Place(number_bathrooms=7)

        self.assertIsInstance(place.number_bathrooms, int)

    def test_max_guest_int(self):
        """test to check max_guest value int"""

        place = Place(max_guest=8)

        self.assertIsInstance(place.max_guest, int)

    def test_latitude_float(self):
        """test to check latitude float value"""

        place =Place(latitude=100.0)

        self.assertIsInstance(place.latitude, float)

    def test_longitude_float(self):
        """Test to check longitude float value"""

        place = Place(longitude=-99.8)

        self.assertIsInstance(place.longitude, float)

    def test_amenity_ids_list(self):
        """test amenity_is is list"""

        place = Place(amenity_ids=["1", "2"])

        self.assertIsInstance(place.amenity_ids, list)

    def test_numbers_positive_int(self):
        """test to check number of rooms positive ang greater than 0"""

        place = Place(number_rooms=5)

        self.assertTrue(place.number_rooms > 0)

    def test_number_bathrooms_positive_int(self):
        """Test that no of bathroom greater than 0"""

        place = Place(number_bathrooms=7)

        self.assertTrue(place.number_bathrooms > 0)

    def test_max_guest_positive(self):
        """test that max guests positive"""

        place = Place(max_guest=6)

        self.assertTrue(place.max_guest > 0)

    def test_price_by_night_positive(self):
        """test price by night positive"""

        place = Place(price_by_night=4500)

        self.assertTrue(place.price_by_night > 0)

    def test_Place_sublass_BaseModel(self):
        """test to check if place is subclass of BaseModel"""
        
        self.assertTrue(issubclass(Place, BaseModel))

#destructor tests
    def test_destructor(self):
        """unittest that checks whether its destructed and set to zero"""
        
        place = Place()
        
        del place

        with self.assertRaises(NameError):
            place        

if __name__ == "__main__":
    unittest.main()
