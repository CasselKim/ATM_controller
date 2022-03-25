'''
request.py
===========
this module is for communication with the BANK API.

Methods:
    check_valid_PIN(PIN : uuid4) -> bool
    check_valid_account_form(account : str) -> bool
    check_valid_account(PIN : uuid4, account : str) -> bool
    get_accounts(PIN : uuid4) -> LIST[str]
    get_account_content(PIN : uuid4, account : str)

Todo:    
    errors
      - custom errors for this project
'''
