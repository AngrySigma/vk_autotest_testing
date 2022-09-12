import pytest
from math import isinf, isnan


@pytest.fixture
def inf():
    return float('inf')


@pytest.fixture
def nan():
    return float('nan')


@pytest.mark.parametrize('test_input, result',
                         [('1.1 + 1.2', 2.3),
                          ('1.4 - 1.8', -0.40000000000000013),
                          ('1000.5 * -10000000.1', -10005000100.05),
                          ('11.11 / 1.1', 10.099999999999998),
                          ('10.1 ** 11.1', 140594149528.10672)])
def test_float_float(test_input, result):
    assert eval(test_input) == result


@pytest.mark.parametrize('test_input, result',
                         [('1.1 + 1', 2.1), ('10000.1 - 10000000', -9989999.9),
                          ('10.11 * 10', 101.1),
                          ('10000000.1111 / 1000', 10000.0001111),
                          ('100.1 ** 10', 1.0100451202102516e+20)])
def test_float_int(test_input, result):
    assert eval(test_input) == result


@pytest.mark.parametrize('test_input', ['isinf(inf + 1)',
                                        'isinf(inf - 1)',
                                        'isinf(inf * 10.1)',
                                        'isinf(inf / 10.1)',
                                        'isinf(inf + inf)',
                                        'isinf(inf - 1e100)',
                                        'isnan(inf - 1e100000)',
                                        'isinf(1e1000)',
                                        'isnan(inf - nan)',
                                        'isnan(inf + nan)'
                                        ])
def test_infinity(test_input, inf, nan):
    assert eval(test_input)
