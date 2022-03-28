'''
errors.py
===========
this module provide error handling and writing logs.

Attributes:
    error_handler
      
Example:
    @error_handler
'''

from typing import Dict, Any, Callable
from datetime import datetime
import re
import os

def error_handler(func: Callable):
    '''
    Catch Error and leave logs on logfile.log
    ---
    
    Args:
        func : Callable

    '''
    
    # import logging libarary
    import logging

    # Creating and Configuring Logger
    Log_Format = "%(levelname)s %(asctime)s - %(message)s at %(filename)s"
    logging.basicConfig(filename = "logfile.log",
                        filemode = "w",
                        format = Log_Format, 
                        level = logging.ERROR)
    logger = logging.getLogger()

    # make wrapper
    def wrapper(*args: Any, **kwargs: Dict[str, Any]) :
        already = False
        try : 
            result = func(*args, **kwargs) # execute function with try-except
        except Exception as e : 
            logger.error(func.__name__+"({}) failed".format(*args)+" "+str(e)) # leave log if errors
            result = False
            already = True
        
        # leave log if not error but empty result
        if result == False and already == False : 
            logger.error(func.__name__+"({}) failed".format(*args)) # write log
        return result
    
    return wrapper