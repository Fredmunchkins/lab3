import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_greater_10():
    input_arr = [23, 1, 56, 17, 34, 78, 4, 45, 12, 6, 89, 32]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == 1

def test_bubble_sort_zero():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == 0

def test_bubble_sort_not_integer():
    input_arr = ["a" , "b" , "c"]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == 2

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])