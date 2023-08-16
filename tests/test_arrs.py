from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([1, 2, 3], -1) is None
    assert arrs.get([], 0) is None
    assert arrs.get([1, 2, 3], 5, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0, 4) == [1, 2, 3, 4]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([1, 2, 3, 4], 2) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 1, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 3, 1) == []
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_boundary_cases():
    assert arrs.my_slice([1, 2, 3, 4], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4], 0, 5) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -5, 2) == [1, 2]


if __name__ == "__main__":
    test_get()
    test_slice()
    test_boundary_cases()
