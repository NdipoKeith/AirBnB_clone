#!/usr/bin/python3
"""testcase for User Class
    test_case:
        calidatng functions
        constructor functions
"""
import unittest
import models
import json
import re
from models import storage
from models.user import User
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class testUser(unittest.TestCase):

    def setUp(self):
        """sets up test methods"""
        
        pass

#    def tearDown(self):
        """Tears down a method"""

#        pass

#constructor without argument
    def test_constructor_no_arg(self):
        """constructor initialized with no args"""

        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

#constructor with arguments
    def test_init(self):
        """Test to see whether the set user details are the correct"""

        user = User(email="njagidave@gmail.com", password="passwrd", first_name="Dave", last_name="Njagi")

        self.assertEqual(user.email, "njagidave@gmail.com")
        self.assertEqual(user.password, "passwrd")
        self.assertEqual(user.first_name, "Dave")
        self.assertEqual(user.last_name, "Njagi")

    def test_set_email(self):
        """test to see if the set email is the correct output email"""
        
        user = User(email="njagidave@gmail.com")
        
        self.assertEqual(user.email, "njagidave@gmail.com")

    def test_update_email(self):
        """test to check whether the retrieved mail is the correct one"""
        user = User(email="njagidave@gmail.com")
        
        user.email = "elvis@yahoo.com"

        retrieved_mail = user.email
        
        self.assertEqual(user.email, retrieved_mail)

    def test_set_password(self):
        """test to check for the set password"""
        user = User()

        user = User(password="passwrd")

        self.assertEqual(user.password, "passwrd")

    def test_getpassword(self):
        """Test to check if the retrieved password is true"""

        user = User(password="passwrd")
        
        user.password = "12345"

        pass_wd = user.password
        
        self.assertEqual(user.password, pass_wd)

    def test_set_firstname(self):
        """Test to check whether set first name is true"""
        
        user = User()

        user = User(first_name="Dave")
        self.assertEqual(user.first_name, "Dave")

    def test_get_first_name(self):
        """test to check whether retrieved first name True"""

        user = User()

        user.firt_name = "Elvis"
        
        name1 = user.first_name

        self.assertEqual(user.first_name, name1)

    def test_set_last_name(self):
        """Test to check whether set last name True"""
        
        user = User(last_name="Njagi")
        
        self.assertEqual(user.last_name, "Njagi")

        
    def test_update_user_name(self):
        """test for updated user last name"""
            
        user = User(last_name="Njagi")

        user.last_name = "Kim"

        self.assertEqual(user.last_name, "Kim")

    
    def test_save_retrieve_update_to_json(self):
        """Test to check whether the info is saved"""
       
        user = User(email="davenjagi@gmail.com", password="passwrd", first_name="Dave", last_name="Njagi")
        
        with open("user.json", "w") as f:
            json.dump(user.email, f)
            json.dump(user.password, f)
            json.dump(user.first_name, f)
            json.dump(user.last_name, f)

        with open("user.json", "r") as f:
             user_json = json.load

        user_json_file = User(password="passwrd")
        user_json_file.password = "12345"

        with open("user.json", "w") as f:
            json.dump(user_json_file.password, f)

        os.remove("user.json")

    def test_user_subclass_basemodel(self):
        """test is a subclass of BaseModel"""

        self.assertTrue(issubclass(User, BaseModel))

#testdowndeconstructor
    def test_teardown(self):
        """test for del method for class"""
        
        user = User()
        
        del user

        with self.assertRaises(NameError):
            user.name

        with self.assertRaises(NameError):
            user.email
        
        with self.assertRaises(NameError):
            user.password

        with self.assertRaises(NameError):
            user.last_name

        with self.assertRaises(NameError):
            user.first_name

if __name__ == "__main__":
    unittest.main()
