'''
controller.py
===========
this module provide exchange API of the BANK API.

Attributes:
    Card
      - PIN Number -> str (uuid4)(not null)
      - Account_activate -> str (000-00-000000)
      - PIN_available_check() -> bool
      - Account_available_check() -> bool
      
Example:
    card_obj = Card("550e8400-e29b-41d4-a716-446655440000")
    card_obj.Account_activate = "501-69-106992"

Todo:
    method
      - request to BANK API for get accounts
      - request to get display blance, deposit and withdraw
      
    errors
      - custom errors for this project
'''

from uuid import uuid4
import requests

class Card : 
    def __init__(self, PIN:uuid4):
        '''
        Note:
            PIN number for test : "550e8400-e29b-41d4-a716-446655440000"
            Account for test : "000-00-000000"
        '''
        self.PIN = PIN
        self.Account_activate = None

