def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer Only"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(n // 10)


if __name__ == '__main__':
    print(sum_of_digits(-157))
