from utils3 import sum_of_even_squares


def test_sum_of_even_squares():  # defining a test function to test the function sum_of_even_squares
    # test case 1: List with even numbers
    assert sum_of_even_squares([2, 4, 6, 8]) == 120

    # test case 2: List with odd numbers
    assert sum_of_even_squares([1, 3, 5, 7]) == 0

    # test case 3: Empty list
    assert sum_of_even_squares([]) == 0

    # test case 4: List with mixed numbers
    assert sum_of_even_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 120

    print("All test cases passed successfully.")
