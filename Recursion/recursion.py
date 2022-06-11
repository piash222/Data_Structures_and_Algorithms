import re

def recursive_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_method(n - 1)
        print(n)


def first_method():
    second_method()
    print("I am the first first method")
    re.search('',string='')


def second_method():
    third_method()
    print("I am the second method")


def third_method():
    fourth_method()
    print("I am the third method")


def fourth_method():
    print("I am the fourth method")


if __name__ == '__main__':
    first_method()
    # recursive_method(10)
