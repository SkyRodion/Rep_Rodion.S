
# task 1

def sum_range(start, end):
    if start > end:
        start, end = end, start
    x = 1
    num = 0
    for i in range(start, end + x):
        num += i
    return num


# start = int(input('Provide Start number: '))
# end = int(input('Provide End number: '))
# result = sum_range(start, end)
# print(result)

# task 2

def square(side_of_square):    # не зрозумів, чому якщо написати def square(side_of_square: float): в мене віпадє помилка?
    P = side_of_square*4
    S = side_of_square*side_of_square
    D = side_of_square*(pow(side_of_square, 0.5))
    res = print(f'Perimeter of a square: {P} ;''\n'
                f'Area of the square: {S}; ''\n'
                f'Diagonal of a square: {D} ' '\n')
    return res

# side = input('Provide side of square: ')
# square(float(side))


# task 3
def user_input():
    input1 = input("Enter a value: ")
    return input1

def print_user_input_type(user_input):
    try:
        data_type = type(eval(user_input))
        print(f"User is going to work with {data_type}")
    except:
        print("Invalid input. Please enter a valid data type.")


input1 = user_input()
print(input1)

user_input2 = user_input()
print_user_input_type(user_input2)