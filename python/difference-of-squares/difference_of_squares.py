def difference(num):
    return square_of_sum(num) - sum_of_squares(num)


def square_of_sum(num):
    l = [(n + 1) for n in range(num)]

    return sum(l)**2


def sum_of_squares(num):
    return sum(((n + 1)**2) for n in range(num))
