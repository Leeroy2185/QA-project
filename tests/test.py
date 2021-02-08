import unittest
from flask import url_for
from flask_testing import TestCase

from app import app ,db , User, Car

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLACHEMY_DATABASE_URI="sqlite:///")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all() 

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,200)     




     


   
        
    


    
