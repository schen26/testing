from testing import count


def test_count_zeros():
    assert count.count([0, 0, 0], 0) == 3


def test_count_string():
    assert count.count(["a", "a", "a"], "a") == 3


def test_sum_of_1_and_1():
    assert count.sum_of(1, 1) == 2


def test_sum_of_2_and_2():
    assert count.sum_of(2, 2) == 4


def test_sum_of_decimals():
    assert count.sum_of(1.0, 2.1) == 3.1
