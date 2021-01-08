import pytest
import json
import numpy as np

from yarr_tools.utils import retriever
from yarr_tools.utils.yarr_histo import YarrHisto1d, YarrHisto2d


@pytest.fixture
def simple_histo1d():
    return """{
    "Data": [0,1,2,3,4,5,6,7,8,9],
    "Name": "TestDist",
    "Overflow": 0.0,
    "Type": "Histo1d",
    "Underflow": 0.0,
    "x": {
        "AxisTitle": "x title",
        "Bins": 10,
        "High": 100.5,
        "Low": 0.5
    },
    "y": {
        "AxisTitle": "y title"
    },
    "z": {
        "AxisTitle": "z title"
    }
}
"""


@pytest.fixture
def simple_histo1d_dict(simple_histo1d):
    return json.loads(simple_histo1d)


@pytest.fixture
def simple_histo2d():
    return """{
    "Data": [[1,2,3],[4,5,6],[7,8,9]],
    "Name": "TestMap",
    "Overflow": 0.0,
    "Type": "Histo2d",
    "Underflow": 0.0,
    "x": {
        "AxisTitle": "x title",
        "Bins": 3,
        "High": 3.5,
        "Low": 0.5
    },
    "y": {
        "AxisTitle": "y title",
        "Bins": 3,
        "High": 3.5,
        "Low": 0.5
    },
    "z": {
        "AxisTitle": "z title"
    }
}
"""


@pytest.fixture
def simple_histo2d_dict(simple_histo2d):
    return json.loads(simple_histo2d)


def test_histo1d_load_json(simple_histo1d):
    h = json.loads(simple_histo1d)
    assert isinstance(retriever.from_yarr(h), YarrHisto1d)


def test_histo2d_load_json(simple_histo2d):
    h = json.loads(simple_histo2d)
    assert isinstance(retriever.from_yarr(h), YarrHisto2d)


def test_histo1d_load_file(simple_histo1d):
    with open("tmp.json", "w") as ofile:
        ofile.write(simple_histo1d)
    assert isinstance(retriever.from_yarr("tmp.json"), YarrHisto1d)


def test_histo2d_load_file(simple_histo2d):
    with open("tmp.json", "w") as ofile:
        ofile.write(simple_histo2d)
    assert isinstance(retriever.from_yarr("tmp.json"), YarrHisto2d)


def test_histo1d_shape(simple_histo1d_dict):
    h = retriever.from_yarr(simple_histo1d_dict)
    assert h.histogram.shape == (10,)


def test_histo2d_shape(simple_histo2d_dict):
    h = retriever.from_yarr(simple_histo2d_dict)
    assert h.histogram.shape == (3, 3)


def test_create_histo1d():
    data = np.array([1.0, 2.0, 3.0])
    h = YarrHisto1d(data)
    assert list(h.histogram) == list(data)


def test_histo1d_add():
    data0 = np.array([1.0, 1.0, 1.0])
    data1 = np.array([1.0, 1.0, 1.0])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 = h0 + h1
    assert list(h0.histogram) == [2.0, 2.0, 2.0]


def test_histo1d_iadd():
    data0 = np.array([1.0, 1.0, 1.0])
    data1 = np.array([1.0, 1.0, 1.0])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 += h1
    assert list(h0.histogram) == [2.0, 2.0, 2.0]


def test_histo1d_add_number():
    data = np.array([1.0, 1.0, 1.0])
    h = YarrHisto1d(data)
    h += 3
    assert list(h.histogram) == [4.0, 4.0, 4.0]


def test_histo1d_sub():
    data0 = np.array([1.0, 1.0, 1.0])
    data1 = np.array([1.0, 1.0, 1.0])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 = h0 - h1
    assert list(h0.histogram) == [0.0, 0.0, 0.0]


def test_histo1d_isub():
    data0 = np.array([1.0, 1.0, 1.0])
    data1 = np.array([1.0, 1.0, 1.0])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 -= h1
    assert list(h0.histogram) == [0.0, 0.0, 0.0]


def test_histo1d_sub_number():
    data = np.array([4.0, 4.0, 4.0])
    h = YarrHisto1d(data)
    h -= 3
    assert list(h.histogram) == [1.0, 1.0, 1.0]


def test_histo1d_mul():
    data = np.array([1.0, 1.0, 1.0])
    h = YarrHisto1d(data)
    h = h * 2
    assert list(h.histogram) == [2.0, 2.0, 2.0]


def test_histo1d_imul():
    data = np.array([1.0, 1.0, 1.0])
    h = YarrHisto1d(data)
    h *= 2
    assert list(h.histogram) == [2.0, 2.0, 2.0]


def test_histo2d_add():
    data0 = np.array([[1.0, 1.0], [1.0, 1.0]])
    data1 = np.array([[1.0, 1.0], [1.0, 1.0]])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 = h0 + h1
    assert (h0.histogram == np.array([[2.0, 2.0], [2.0, 2.0]])).all()


def test_histo2d_iadd():
    data0 = np.array([[1.0, 1.0], [1.0, 1.0]])
    data1 = np.array([[1.0, 1.0], [1.0, 1.0]])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 += h1
    assert (h0.histogram == np.array([[2.0, 2.0], [2.0, 2.0]])).all()


def test_histo2d_add_number():
    data = np.array([[1.0, 1.0], [1.0, 1.0]])
    h = YarrHisto1d(data)
    h += 3
    assert (h.histogram == np.array([[4.0, 4.0], [4.0, 4.0]])).all()


def test_histo2d_sub():
    data0 = np.array([[1.0, 1.0], [1.0, 1.0]])
    data1 = np.array([[1.0, 1.0], [1.0, 1.0]])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 = h0 - h1
    assert (h0.histogram == np.array([[0.0, 0.0], [0.0, 0.0]])).all()


def test_histo2d_isub():
    data0 = np.array([[1.0, 1.0], [1.0, 1.0]])
    data1 = np.array([[1.0, 1.0], [1.0, 1.0]])
    h0 = YarrHisto1d(data0)
    h1 = YarrHisto1d(data1)
    h0 -= h1
    assert (h0.histogram == np.array([[0.0, 0.0], [0.0, 0.0]])).all()


def test_histo2d_sub_number():
    data = np.array([[4.0, 4.0], [4.0, 4.0]])
    h = YarrHisto1d(data)
    h -= 3
    assert (h.histogram == np.array([[1.0, 1.0], [1.0, 1]])).all()


def test_histo2d_mul():
    data = np.array([[1.0, 1.0], [1.0, 1.0]])
    h = YarrHisto1d(data)
    h = h * 2
    assert (h.histogram == np.array([[2.0, 2.0], [2.0, 2.0]])).all()


def test_histo2d_imul():
    data = np.array([[1.0, 1.0], [1.0, 1.0]])
    h = YarrHisto1d(data)
    h *= 2
    assert (h.histogram == np.array([[2.0, 2.0], [2.0, 2.0]])).all()
