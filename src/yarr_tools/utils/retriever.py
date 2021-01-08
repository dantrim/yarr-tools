import numpy as np
from .yarr_histo import YarrHisto1d, YarrHisto2d
import json
from typing import Union
from pathlib import Path

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


def from_yarr(
    input_file: Union[dict, str, Path]
) -> Union[YarrHisto1d, YarrHisto2d, None]:

    if isinstance(input_file, str) or isinstance(input_file, Path):
        try:
            with open(input_file, "r") as infile:
                json_data = json.load(infile)
        except (FileNotFoundError, ValueError):
            logger.exception(f'Failed to load JSON data from input file "{input_file}"')
            return None
    elif isinstance(input_file, dict):
        json_data = input_file

    return {"Histo1d": histo1d_from_yarr, "Histo2d": histo2d_from_yarr}[
        json_data["Type"]
    ](json_data)


def histo1d_from_yarr(input_file: Union[dict, str, Path]) -> Union[YarrHisto1d, None]:

    if isinstance(input_file, str) or isinstance(input_file, Path):
        try:
            with open(input_file, "r") as infile:
                json_data = json.load(infile)
        except (FileNotFoundError, ValueError):
            logger.exception(f'Failed to load JSON data from input file "{input_file}"')
            return None
    elif isinstance(input_file, dict):
        json_data = input_file
    return YarrHisto1d(np.array(json_data["Data"]), json_data)


def histo2d_from_yarr(input_file: Union[dict, str, Path]) -> Union[YarrHisto2d, None]:

    if isinstance(input_file, str) or isinstance(input_file, Path):
        try:
            with open(input_file, "r") as infile:
                json_data = json.load(infile)
        except (FileNotFoundError, ValueError):
            logger.exception(f'Failed to load JSON data from input file "{input_file}"')
            return None
    elif isinstance(input_file, dict):
        json_data = input_file
    return YarrHisto2d(np.array(json_data["Data"]), json_data)
