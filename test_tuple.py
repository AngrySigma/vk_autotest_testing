import pytest


@pytest.fixture
def test_tuple():
    return 1, 1000, -1


@pytest.mark.parametrize('test_index, expected',
                         [(0, 1), (2, -1), (-1, -1), (-3, 1), (True, 1000)])
def test_indices(test_index, expected, test_tuple):
    assert test_tuple[test_index] == expected


@pytest.mark.parametrize('test_index, expected_error',
                         [(3, IndexError), (-4, IndexError), (100, IndexError),
                          (-100, IndexError), ('1', TypeError),
                          (None, TypeError), ((1,), TypeError)])
def test_index_out_of_bounds(test_index, expected_error, test_tuple):
    try:
        assert test_tuple[test_index]
        pytest.fail()
    except Exception as e:
        assert isinstance(e, expected_error)


@pytest.mark.parametrize('test_input',
                         [1, '1', 'a', None, 'None', True, 'True', [0, 1],
                          '[0, 1]', {0, 1}, {0: 1, 2: 3},
                          object])
def test_data_types(test_input):
    test_tuple = tuple([1, '1', 'a', None, 'None', True, 'True', [0, 1],
                        '[0, 1]', {0, 1}, {0: 1, 2: 3},
                        object])
    assert test_input in test_tuple
