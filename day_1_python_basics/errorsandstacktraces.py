#stack traces 
import logging
logging.basicConfig(level=logging.ERROR)
try:
    10 / 0
except Exception as e:
    logging.error("Error occurred", exc_info=True) #exc_info=True will print the stack trace
