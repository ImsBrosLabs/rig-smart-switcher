# import os
# import sys

# root_folder = os.path.abspath(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root_folder)
# from config.init_config import config_file as config

import requests
from logzero import logger


def retrieve_weather(latitude, longitude):
    logger.info("Retrieving data from Open Meteo API...")
    url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true".format(
        latitude = latitude, longitude = longitude)
    logger.info("...The contructed URL is %s...", url)

    with requests.get(url) as res:
        try:

            # The Requests package doesn't catch HTTP errors (if one occured) implicitly, hence this line 👇.
            res.raise_for_status()

            json_res = res.json()
            logger.info("...Open Meteo data retrieved ! => %s", json_res)

            return json_res
        except requests.exceptions.HTTPError as exception:
            raise exception
