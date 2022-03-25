'''
Controller.py
===========

제목을 정할 때는 기존과 같습니다. `==`로 제목을 `--`로 소제목을
표현합니다. `참고해야 할 하이퍼링크`_ 가 있다면 아래에 url 정의를
할 수 있습니다.

Attributes:
    Card
      - PIN Number -> str (uuid)(not null)
      - Account_activate -> str (000-00-000000)
      
Example:
    card_obj = Card("550e8400-e29b-41d4-a716-446655440000")
    card_obj.Account_activate = "501-69-106992"

Todo:
    * 앞으로 할 것의 목록
    * `Todo`는 모듈이나 패키지, 함수, 클래스 등에 자유롭게
        사용할 수 있습니다.
    * 사용자 입장에서 서술하는 것이 좋습니다.
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
        



