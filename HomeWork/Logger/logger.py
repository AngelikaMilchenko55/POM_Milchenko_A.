import logging
import calculator

logging.basicConfig(level='INFO', filename='calculator_log.log', format="[%(asctime)s] - %(pathname)s : %(funcName)s - %(levelname)s: %(message)s",
                    datefmt='%H:%M:%S %d-%m-%Y')
logger = logging.getLogger()#логгер

def main(name):
    logger.debug(f'Enter in the main() function: name={name}')

if __name__ == '__main__':
    main('calculator')
    calculator.calculator(5,0)
    #logger.error("error")