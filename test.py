from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_word(self):
        """Check if word is valid"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] =  [["L", "A", "W", "N", "B"], 
                                 ["A", "P", "P", "L", "E"], 
                                 ["P", "A", "L", "E", "T"], 
                                 ["W", "O", "R", "K", "L"], 
                                 ["Y", "I", "E", "S", "T"]]
        response = self.client.get('/check?word=pal')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get('/check?word=mad')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_non_english_word(self):
        """Test if word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/check?word=asdf')
        self.assertEqual(response.json['result'], 'not-word')
