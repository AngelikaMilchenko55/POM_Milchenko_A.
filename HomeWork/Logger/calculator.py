import  logging

logger = logging.getLogger(__name__)

def calculator(a,b):
    logging.info("start calculator()")
    try:
        print(a,"+", b, "=", a+b)
        logging.info("addition done")
        print(a,"-", b, "=", a-b)
        logging.info("subtraction done")
        print(a,"*", b, "=", a*b)
        logging.info("multiplication done")
        print(a,"/", b, "=", a/b)
        logging.info("division done")
    except ZeroDivisionError:
        logging.error("ZeroDivisionError", exc_info=True)
    logging.info("end calculator()")

