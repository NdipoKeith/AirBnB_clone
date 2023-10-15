#!/usr/bin/python3

"""testunit or file file_storage.py
    test classes:
            construct instantiation withour args
            destructor
"""

import models
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity
from unittest.mock import patch

class TestCaseFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()

    def teardown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_invalid_obj(self):
        with self.assertRaises(TypeError):
            self.file_storage.save(object())

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_reload_midding_file(self, mock_open):
            self.file_storage.reload()

if __name__ == "__main__":
    unittest.main()
