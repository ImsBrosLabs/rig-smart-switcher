#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Sangimed"
__version__ = "0.0.1"
__license__ = "MIT"

from PyP100 import PyP110
from config.init_config import config_file as config
from logzero import logger


def main():
    """ 
    IF plug is ON AND at least one of the GPU exceeds a specified temp 
    THEN turn off the smart plug

    IF smart plug is off and the current temp is below a specified a certain amount
    THEN turn on the smart plug

    #TODO Add an ON/OFF switch that allows to control eithrer the script is ON or OFF.
    #TODO log EVERYTHING !
    """

    logger.info("Creating a P110 plug object...")

    p110 = PyP110.P110(config['p110']['ip'], config['p110']
                       ['email'], config['p110']['password'])

    logger.info("...P110 plug object created !")

    logger.info("Creating the cookies required for further methods...")
    p110.handshake()
    logger.info("...Cookies created !")

    logger.info("Sending credentials to the plug and creating AES Key and IV for further methods...")
    p110.login()
    logger.info("...Credentials sent.")

    logger.info("Turning ON the p110 smart plug...")
    p110.turnOn()
    logger.info("...P110 is ON !")

    logger.info(p110.getDeviceInfo())  # Returns dict with all the energy usage


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
