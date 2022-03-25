'''
request.py
===========
this module is for communication with the BANK API.
Please note that this is not the actual connection.
In order to connect real BANK API, Do edit this part.

Methods:
    check_valid_PIN(PIN : uuid4) -> bool
    check_valid_account(PIN : uuid4, account : str) -> bool
    check_valid_account_form(account : str) -> bool
    get_accounts(PIN : uuid4) -> LIST[str]
    get_account_content(PIN : uuid4, account : str) -> Dict[str,int]

Todo:    
    errors
      - custom errors for this project
'''

from typing import List, Dict, Any
from uuid import uuid4
import re

def check_valid_PIN(PIN : uuid4) -> bool : 
    '''
    Send request to BANK API for check availability of card's PIN number.
    ---
    
    Args:
        PIN : uuid4

    '''

    # make RESTFUL API for request availibility of PIN number to BANK API
    url = "BANK_RESTFUL_API"
    headers = "Headers"
    params = {"PIN" : PIN}

    # PIN number for test
    if PIN == "550e8400-e29b-41d4-a716-446655440000" : 
        return True
    else : 
        return False

def check_valid_account(PIN : uuid4, account : str) -> bool : 
    '''
    Send request to BANK API for check availability of user's account.
    ---
    
    Args:
        PIN : uuid4
        account : str (format : 000-00-000000)
        
    '''

    # make RESTFUL API for request availibility of user's account to BANK API
    url = "BANK_RESTFUL_API"
    headers = "Headers"
    params = {"PIN" : PIN, "Account" : account}

    # Account for test
    if PIN == "000-00-000000" : 
        return True
    else : 
        return False
    
def check_valid_account_form(account : str) -> bool : 
    '''  
    check valid account form with regex
    ---
    
    Args:
        account : str
        
    '''
    
    account_regex = re.compile('[0-9]{3}-[0-9]{2}-[0-9]{6}')
    result = account_regex.match(account)
    if result : 
        return True
    else : 
        return False
    
def get_accounts(PIN : uuid4) -> List[str] : 
    '''  
    get account list with PIN from BANK API
    ---
    
    Args:
        PIN : uuid4
    
    '''
    # make RESTFUL API for request availibility of user's account to BANK API
    url = "BANK_RESTFUL_API"
    headers = "Headers"
    params = {"PIN" : PIN}
    
    # test input
    with open('./test_accounts.txt','r') as f : 
        test_input = f.read()
    return test_input.split('\n')
    
    
def get_account_content(PIN : uuid4, account : str) -> Dict[str,int] : 
    '''  
    get account list with PIN from BANK API
    ---
    
    Args:
        PIN : uuid4
        account : str (format : 000-00-000000)
        
    Returns:
        contents : Dict(str,int)
        {
            'balance' : int,
            'deposit' : int,
            'withdraw' : int
        }
    
    '''
    # make RESTFUL API for request availibility of user's account to BANK API
    url = "BANK_RESTFUL_API"
    headers = "Headers"
    params = {"PIN" : PIN, "account" : account}
    
    # test input
    with open('./test_account_contents.txt','r') as f : 
        test_input = f.read()
    contents = dict()
    contents["balance"], contents["deposit"], contents["withdraw"] = test_input.split(',')
    return contents

# test case
if __name__ == '__main__' : 
    PIN = "550e8400-e29b-41d4-a716-446655440000"
    account = "000-00-000000"
    print(get_accounts(PIN))
    print(get_account_content(PIN, account))