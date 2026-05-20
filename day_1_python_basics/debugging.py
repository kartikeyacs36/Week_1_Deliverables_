#using print statements for debugging
def add(a,b):
    print("a =", a) #print statement to debug the value of a
    print("b =", b)
    print("expected  a + b =", a+b)
    return a-b #intentional error to understand debugging
result = add(10,5)
print(result) #expected output is 15 , but we will get 5

#using logging
import logging
logging.basicConfig(level=logging.DEBUG)  #if level is not provided ; then default will be warning level
def divide(a,b):
    logging.info(f"a = {a} , b = {b}")
    if b == 0:
        logging.error("cannot didive with zero")
        return None
    else:
        result = a / b
        logging.info(f"{a} / {b} = {result}")
        return result
result = divide(10,0)
print(result)

#Levels of debugging
#logging.debug("Debug: checking variables")
#logging.info("Info: program started")
#logging.warning("Warning: low disk space")
#logging.error("Error: file missing")
#logging.critical("Critical: system failure")