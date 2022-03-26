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
from . import request
from . import atmIO

class Card : 
    def __init__(self, PIN:uuid4):
        '''
        Note:
            PIN number for test : "550e8400-e29b-41d4-a716-446655440000"
            Account for test : "000-00-000000"
        '''
        self.PIN = PIN
        self.Account_activate = None

if __name__ == '__main__' : 
  
  while True : 
    # read card
    PIN = atmIO.read_Card()
    
    # check valid PIN number
    if request.check_valid_PIN(PIN) == True : 
      # create Card object
      card = Card(PIN)
      break
    else : 
      # if invaild PIN number
      atmIO.split_Card()
    
  # get accounts
  accounts = request.get_accounts(card.PIN)
  
  # display accounts list
  atmIO.display_accounts(accounts)
  
  # get selected account
  account = atmIO.get_selected_account()
  card.Account_activate = account
  
  # check valid account
  if request.check_valid_account(card.Account_activate)==True :
    account_content = request.get_account_content(card.PIN, card.Account_activate)
    atmIO.display_account_content(account_content)
  else : 
    # [TODO] replace with error handler
    print("cannot read account contents!!")