'''
atmIO.py
===========
this module is for communication with the ATM.

Methods:
    split_Card() -> bool
    read_Card() -> str
    display_accounts(accounts : List[str])
    get_selected_account() -> str
    display_account_content(account_content : Dict[str, int])

Todo:       
    errors
      - custom errors for this project
'''

from typing import List, Dict, Any
from uuid import uuid4
import re


def split_Card() -> bool : 
    
    '''
    split Card from ATM's card reader
    ---
    
    Note : 
        This is just for the test.
        So replace splt_method with ATM's card reader later. 
    '''
    return True

def read_Card() -> uuid4 : 
    
    '''
    read Card's PIN number from ATM's card reader
    ---
    
    Note : 
        This is just for the test.
        So replace f_read with ATM's card reader later. 
    '''
    
    with open('./test_card_input.txt','r') as f : 
        test_input = f.read()
    return test_input
        
def display_accounts(accounts : List[str]) : 
        
    '''
    display accounts on ATM screen.
    check every account for valid account form
    ---
    
    Args:
        accounts : List[str]
        
    Note : 
        This is just for the test
        So replace print with display on screen later. 
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
        This is just for the test
        So replace f_read with user's screen touch later. 
        
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
        This is just for the test.
        So replace print with display on screen later. 
        
    '''
    
    try : 
        for key,value in account_content.items() : 
            print("{} : {}".format(key,value))
            
    #[TODO] add custom exception
    except Exception as e : 
        print("Invalid account contents form")

