'''
atmIO.py
===========
this module is for communication with the ATM.

Methods:
    read_Card() -> str
    [Todo] is_valid_PIN(PIN : uuid4) -> bool
    [Todo] is_valid_account_form(account : str) -> bool
    [Todo] is_valid_account(account : str) -> bool
    display_accounts(accounts : List[str])
    get_selected_account() -> str
    display_account_content(account_content : Dict[str, int])

Todo:   
    every is_valid_* methods should be held in request.py.
    they don't have to be checked twice at server and client
    
    errors
      - custom errors for this project
'''

from typing import List, Dict, Any
from uuid import uuid4
import re

def read_Card() -> uuid4 : 
    
    '''
    read Card's PIN number from ATM's card reader
    ---
    
    Note : 
        This is just for the test, so replace f_read with ATM's card reader later. 
        
    '''
    
    with open('./test_card_input.txt','r') as f : 
        test_input = f.read()
    return test_input

def is_valid_PIN(PIN : uuid4) -> bool : 
    
    '''  
    check valid PIN value
    ---
    
    Args:
        account : str
        
    Note : 
        This is just for the test, so replace it with actual API request. 
        
    TODO : 
        it sholud be relocated to request.py
    '''
    
    return PIN == "550e8400-e29b-41d4-a716-446655440000"

def is_valid_account_form(account : str) -> bool : 
    
    '''  
    check valid account form with regex
    ---
    
    Args:
        account : str
        
    Note : 
        This is just for the test, so it must be fit with actual account form. 
        
    TODO : 
        it sholud be relocated to request.py
    '''
    
    account_regex = re.compile('[0-9]{3}-[0-9]{2}-[0-9]{6}')
    result = account_regex.match(account)
    if result : 
        return True
    else : 
        return False
    
def is_valid_account(account : str) -> bool : 
    
    '''  
    check valid account value
    ---
    
    Args:
        account : str
        
    Note : 
        This is just for the test, so replace it with actual API request. 
        
    TODO : 
        it sholud be relocated to request.py
    '''
    
    return account == "000-00-000000"
        
def display_accounts(accounts : List[str]) : 
        
    '''
    display accounts on ATM screen.
    check every account for valid account form
    ---
    
    Args:
        accounts : List[str]
        
    Note : 
        This is just for the test, so replace print with display on screen later. 
    '''
    
    for account in accounts : 
        try : 
            #[TODO] connect with error handling decorator
            assert(is_valid_account_form(account))
            print(account) #display account list
            
        except Exception as e : #[TODO] add custom exception
            print("Invalid account Input")
            continue
        
def get_selected_account() -> str : 
    
    '''
    get selected account from user's screen touch input
    ---
    
    Note : 
        This is just for the test, so replace f_read with user's screen touch later. 
        
    '''
    
    with open('./test_account_input.txt','r') as f : 
        test_input = f.read()
    return test_input
    
def display_account_content(account_content : Dict[str, int]) : 
    
    '''
    display account's content (balance, deposit, withdraw) on ATM screen.
    ---
    
    Args:
        account_content : dictionary[str,int]
        {
            'balance' : int,
            'deposit' : int,
            'withdraw' : int
        }
        
    Note : 
        This is just for the test, so replace print with display on screen later. 
        
    '''
    
    try : 
        for key,value in account_content.items() : 
            print("{} : {}".format(key,value))
            
    #[TODO] add custom exception
    except Exception as e : 
        print("Invalid account contents form")
