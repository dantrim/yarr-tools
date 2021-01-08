import numpy as np
import json

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class YarrHisto1d:
    def __init__(self, data: np.array, metadata: json = {}) -> None:

        # need to check shape
        self._histogram = data
        self._name = ""
        self._overflow = 0.0
        self._underflow = 0.0
        self._type = "Histo2d"
        self._x_label = ""
        self._x_n_bins = 0
        self._x_low_edge = 0
        self._x_high_edge = 0
        self._y_label = ""

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

    def __add__(self, other):
        if isinstance(other, YarrHisto1d):
            assert (
                self._histogram.shape == other.histogram.shape
            ), f"Histograms must have the same shape (self = {self._histogram.shape}, other = {other.histogram.shape})"
            self._histogram += other.histogram
        else:
            assert isinstance(other, (int, float))
            self._histogram += other
        return self

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        if isinstance(other, YarrHisto1d):
            assert (
                self._histogram.shape == other.histogram.shape
            ), f"Histograms must have the same shape (self = {self._histogram.shape}, other = {other.histogram.shape})"
            self._histogram -= other.histogram
        else:
            assert isinstance(other, (int, float))
            self._histogram -= other
        return self

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __mul__(self, other):
        assert isinstance(
            other, (int, float)
        ), "Can only multiple histogram by a number!"
        self._histogram *= other
        return self

    def __imul__(self, other):
        self.__mul__(other)
        return self


class YarrHisto2d:
    def __init__(self, data: np.array, metadata: json = {}) -> None:

        # need to check shape
        self._histogram = data
        self._name = ""
        self._overflow = 0.0
        self._underflow = 0.0
        self._type = "Histo2d"
        self._x_label = ""
        self._x_n_bins = 0
        self._x_low_edge = 0
        self._x_high_edge = 0
        self._y_label = ""
        self._y_n_bins = 0
        self._y_low_edge = 0
        self._y_high_edge = 0
        self._z_label = ""

        # need to add support for jsonschema
        if metadata:
            self._name = metadata["Name"]
            self._overflow = metadata["Overflow"]
            self._underflow = metadata["Underflow"]
            assert self._type == metadata["Type"]

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

    def __add__(self, other):
        if isinstance(other, YarrHisto2d):
            assert (
                self._histogram.shape == other.histogram.shape
            ), f"Histograms must have the same shape (self = {self._histogram.shape}, other = {other.histogram.shape})"
            self._histogram += other.histogram
        else:
            assert isinstance(other, (int, float))
            self._histogram += other
        return self

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __sub__(self, other):
        if isinstance(other, YarrHisto2d):
            assert (
                self._histogram.shape == other.histogram.shape
            ), f"Histograms must have the same shape (self = {self._histogram.shape}, other = {other.histogram.shape})"
            self._histogram -= other.histogram
        else:
            assert isinstance(other, (int, float))
            self._histogram -= other
        return self

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def __mul__(self, other):
        assert isinstance(
            other, (int, float)
        ), "Can only multiple histogram by a number!"
        self._histogram *= other
        return self

    def __imul__(self, other):
        self.__mul__(other)
        return self
