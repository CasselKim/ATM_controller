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
        result = func(*args, **kwargs) # execute wresult
        if result == True : 
            logger.error(func.__name__+"({}) failed".format(*args)) # write log
        return result
    
    return wrapper