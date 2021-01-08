import numpy as np
from .yarr_histo import YarrHisto1d, YarrHisto2d
import json
from typing import Union

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def from_yarr(input_file: str) -> Union[YarrHisto1d, YarrHisto2d, None]:

    try:
        with open(input_file, "r") as infile:
            json_data = json.load(infile)
    except (FileNotFoundError, ValueError):
        logger.exception(f'Failed to load JSON data from input "{input_file}"')
        return None

    return {"Histo1d": histo1d_from_yarr, "Histo2d": histo2d_from_yarr}[
        json_data["Type"]
    ](input_file)


def histo1d_from_yarr(input_file: str) -> YarrHisto1d:
    with open(input_file, "r") as infile:
        json_data = json.load(infile)
    return YarrHisto1d(np.array(json_data["Data"]), json_data)


def histo2d_from_yarr(input_file: str) -> YarrHisto2d:
    with open(input_file, "r") as infile:
        json_data = json.load(infile)
    return YarrHisto2d(np.array(json_data["Data"]), json_data)
