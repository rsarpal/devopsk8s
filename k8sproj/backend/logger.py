import logging
import sys


def backendLogger(message,level):
    # root = logging.getLogger()
    # root.setLevel(logging.DEBUG)

    # handler = logging.StreamHandler(sys.stdout)
    # handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('RSDEBUG %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # root.addHandler(handler)
    # logging.debug(message)

    logging.basicConfig(format='RSDEBUG %(asctime)s - %(name)s -%(levelname)s-%(message)s')
    logging.basicConfig(level=logging.DEBUG)
    if level==0:
        logging.warning(message)
    elif level==1:
        logging.error(message)