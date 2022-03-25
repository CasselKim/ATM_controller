'''
Controller.py
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
        
    def PIN_available_check(self) -> bool : 
        '''
        Note:
            Send request to BANK API for check availability of card's PIN number.
            Please note that this is not for the actual connection to BANK API
            untill the code test is over. In order to connect real BANK API, Do edit this part.
        '''

        # make RESTFUL API for request availibility of PIN number to BANK API
        url = "BANK_RESTFUL_API"
        headers = "Headers"
        params = {"PIN" : self.PIN}
        
        # PIN number for test
        if self.PIN == "550e8400-e29b-41d4-a716-446655440000" : 
            return True
        else : 
            return False
        
    def Account_available_check(self) -> bool : 
        '''
        Note:
            Send request to BANK API for check availability of user's account
            Please note that this is not for the actual connection to BANK API
            untill the code test is over. In order to connect real BANK API, Do edit this part.
        '''

        # make RESTFUL API for request availibility of user's account to BANK API
        url = "BANK_RESTFUL_API"
        headers = "Headers"
        params = {"PIN" : self.PIN, "Account" : self.Account_activate}
        
        # Account for test
        if self.PIN == "000-00-000000" : 
            return True
        else : 
            return False
        



