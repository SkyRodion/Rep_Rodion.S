# task 1

def my_map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result

# # Test for my_map

# x = ['House', "Aplle", "Cat"]
# y = my_map(len, x)
# print(y)

def my_filter(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result

# # Test for my_filter

# def my_func(x):
#   if x <= 10:
#     return False
#   else:
#     return True
#
# n = [-20, 12, 3, 4, 5, 10, 22, 38, 156, 10]
# filter_my_list = my_filter(my_func, n)
# print(filter_my_list)


# task 2


def func_pow(x: int):
    return lambda y: pow(y,x)

# # Test for func_pow

# pow_n = func_pow(int(input('Power x: ')))
# pow_result = pow_n(int(input("Number y: ")))
# print(pow_result)


# task 3

def add(x, y):
    return x + y
def mult(x, y):
    return x * y
def div (x, y):
    if y == 0:
        print("You can't divide by zero")
    return x / y
def minus (x, y):
    return x - y

def main_function():
    funct_name = input("Enter the name of the function to execute: ")
    if funct_name in 'add':
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        print(add(x,y))
    elif funct_name in 'mult':
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        print(mult(x, y))
    elif funct_name in 'div':
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        print(div(x, y))
    elif funct_name in 'minus':
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        print(minus(x, y))
    else:
        print('Incorrect func')


# # Test for main_function
#
# main_function()


