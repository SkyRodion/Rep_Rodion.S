
# task 1

# try:
#  number = float(input('Input number: '))
# except:
#     print('Some error')
# else:
#     if number < 0:
#         raise Exception ('Input positive number')
#     else:
#       print (pow(number, 0.5))
# finally:
#     print('The end')


# task 2

# try:
#     number = float(input('Input number: '))
# except ValueError as error:
#     print(f'Input Error: {error}')
# else:
#     if number < 0:
#         raise Exception ('Input positive number')
#     else:
#       print (pow(number, 0.5))
# finally:
#    print('The end')

# task 3

# while True:
#  try:
#     number = input('Input number (or enter Exit): ')
#     if number == 'Exit':
#         raise SystemExit('Program is closed')
#     number_2 = float(number)
#
#  except ValueError as error:
#     print(f'Input Error: {error}')
#
#  else:
#     if number_2 < 0:
#         raise Exception ('Input positive number')
#     else:
#       print (pow(number_2, 0.5))
#  finally:
#    print('Finally the end')