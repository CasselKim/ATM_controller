from typing import Dict, Any, Callable
from datetime import datetime
import re
import os

def error_handler(func: Callable):
    import logging

    #Creating and Configuring Logger
    Log_Format = "%(levelname)s %(asctime)s - %(message)s at %(filename)s"

    logging.basicConfig(filename = "logfile.log",
                        filemode = "w",
                        format = Log_Format, 
                        level = logging.ERROR)
    logger = logging.getLogger()

    def wrapper(*args: Any, **kwargs: Dict[str, Any]) :
        already = False
        try : 
            result = func(*args, **kwargs) # execute wresult
        except Exception as e : 
            logger.error(func.__name__+"({}) failed".format(*args)+" "+str(e)) # if 
            result = False
            already = True
        
        if result == False and already == False : 
            logger.error(func.__name__+"({}) failed".format(*args)) # write log
        return result
    
    return wrapper