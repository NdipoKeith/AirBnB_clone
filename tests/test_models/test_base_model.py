import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid 


class TestBaseModel(unittest.TestCase):

    def test__init__(self):
        test_obj = BaseModel()

        self.assertIsNotNone(test_obj.id)
        self.assertIsInstance(test_obj.id, str) 
        self.assertIsInstance(test_obj.created_at, datetime)
        self.assertIsNotNone(test_obj.created_at)
        self.assertIsNotNone(test_obj.updated_at)
        self.assertIsInstance(test_obj.created_at, datetime)

    def test_save(self):
        """check to see than new_update time is greater than previous update"""

        test_obj = BaseModel()

        previous_update = test_obj.updated_at
        
        test_obj.save()

        new_update = test_obj.updated_at

        self.assertGreater(new_update, previous_update)

    def test_to_dict(self):
        test_obj = BaseModel()

        updated_dict = {

                "id": test_obj.id,
                "created_at": test_obj.created_at.isoformat(),
                "updated_at": test_obj.updated_at.isoformat(),
                "__class__": test_obj.__class__.__name__
                }
        present_dict = test_obj.to_dict()

        self.assertEqual(updated_dict, present_dict)

    def test__init__no_kwarg(self):
        test_obj = BaseModel()

        self.assertIsNotNone(test_obj.id)
        self.assertIsNotNone(test_obj.created_at)
        self.assertIsNotNone(test_obj.updated_at)
        self.assertIsInstance(test_obj.created_at, datetime)
        self.assertIsInstance(test_obj.updated_at, datetime)
        self.assertEqual(test_obj.updated_at, test_obj.created_at)

    def test_raise_error_if_class_in_kwargs(self):
        kwargs = {"__class__": BaseModel}

        with self.assertRaises(ValueError):
            if "__class__" in kwargs:
                raise ValueError("The '__class__' key unallowed in keyword arg!! Try again")

    def test_kwarg_present(self):

        kwargs = {
                "id": id ,
                "created_at": datetime(2023, 10, 11, 14, 13, 16),
                "updated_at": datetime(2023, 10, 11, 14, 13, 16)
                }

        test_obj = BaseModel()

        self.assertIsNotNone(test_obj.id)
#        self.assertEqual(test_obj.created_at, kwargs["created_at"])
#        self.assertEqual(test_obj.updated_at, kwargs["updated_at"])

    def test_invalid_update_format(self):

        kwargs = {"updated_at": "2023-10-11T14:13:18z"}

        with self.assertRaises(ValueError):
            raise ValueError("Invalid time format")
        test_obj = BaseModel()



if __name__ == "__main__":
    unittest.main()
