import numpy as np
import json

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class YarrHisto1d:
    def __init__(self, data: np.array, metadata: json = {}) -> None:

        # need to check shape
        self._histogram = data
        if metadata:
            # need to add support for jsonschema
            self._name = metadata["Name"]
            self._overflow = metadata["Overflow"]
            self._underflow = metadata["Underflow"]
            self._type = metadata["Type"]

            self._x_label = metadata["x"]["AxisTitle"]
            self._x_n_bins = metadata["x"]["Bins"]
            self._x_low_edge = metadata["x"]["Low"]
            self._x_high_edge = metadata["x"]["High"]

            self._y_label = metadata["y"]["AxisTitle"]

    @property
    def histogram(self):
        return self._histogram

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def x_label(self):
        return self._x_label

    @x_label.setter
    def x_label(self, val):
        self._x_label = val

    @property
    def x_n_bins(self):
        return self._x_n_bins

    @x_n_bins.setter
    def x_n_bins(self, val):
        self._x_n_bins = val

    @property
    def x_low_edge(self):
        return self._x_low_edge

    @x_low_edge.setter
    def x_low_edge(self, val):
        self._x_low_edge = val

    @property
    def x_high_edge(self):
        return self._x_high_edge

    @x_high_edge.setter
    def x_high_edge(self, val):
        self._x_high_edge = val

    @property
    def y_label(self):
        return self._y_label

    @y_label.setter
    def y_label(self, val):
        self._y_label = val


class YarrHisto2d:
    def __init__(self, data: np.array, metadata: json = {}) -> None:

        # need to check shape
        self._histogram = data

        # need to add support for jsonschema
        if metadata:
            self._name = metadata["Name"]
            self._overflow = metadata["Overflow"]
            self._underflow = metadata["Underflow"]
            self._type = metadata["Type"]

            self._x_label = metadata["x"]["AxisTitle"]
            self._x_n_bins = metadata["x"]["Bins"]
            self._x_low_edge = metadata["x"]["Low"]
            self._x_high_edge = metadata["x"]["High"]

            self._y_label = metadata["y"]["AxisTitle"]
            self._y_n_bins = metadata["y"]["Bins"]
            self._y_low_edge = metadata["y"]["Low"]
            self._y_high_edge = metadata["y"]["High"]

            self._z_label = metadata["z"]["AxisTitle"]

    @property
    def histogram(self):
        return self._histogram

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def x_label(self):
        return self._x_label

    @x_label.setter
    def x_label(self, val):
        self._x_label = val

    @property
    def x_n_bins(self):
        return self._x_n_bins

    @x_n_bins.setter
    def x_n_bins(self, val):
        self._x_n_bins = val

    @property
    def x_low_edge(self):
        return self._x_low_edge

    @x_low_edge.setter
    def x_low_edge(self, val):
        self._x_low_edge = val

    @property
    def x_high_edge(self):
        return self._x_high_edge

    @x_high_edge.setter
    def x_high_edge(self, val):
        self._x_high_edge = val

    @property
    def y_label(self):
        return self._y_label

    @y_label.setter
    def y_label(self, val):
        self._y_label = val

    @property
    def y_n_bins(self):
        return self._y_n_bins

    @y_n_bins.setter
    def y_n_bins(self, val):
        self._y_n_bins = val

    @property
    def y_low_edge(self):
        return self._y_low_edge

    @y_low_edge.setter
    def y_low_edge(self, val):
        self._y_low_edge = val

    @property
    def y_high_edge(self):
        return self._y_high_edge

    @y_high_edge.setter
    def y_high_edge(self, val):
        self._y_high_edge = val
