def sum_of_even_squares(
    numbers,
):  # definging a function which calculates the sum of the squares of the even numbers in the list
    sum_of_squares = 0
    for num in numbers:
        if num % 2 == 0:
            sum_of_squares += num**2
    print(sum_of_squares)
    return sum_of_squares
