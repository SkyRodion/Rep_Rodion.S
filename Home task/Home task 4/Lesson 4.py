# task 1

# list_1 = ["john", "marta", "james", "amanda", "marianna"]
# text_1 =' '.join(list_1)
# text_2 = text_1.title()
# list_1 = text_2.split()
# print(list_1)

# task 2

# list_1 = ["FirstItem", "FriendsList", "MyTuple"]
# text_1 = str(list_1)
# text_1 = text_1[0].capitalize() + text_1[1::]
# for a in text_1:
#     if a.isupper():
#         # text_1 = text_1.replace(a, f"_{a.lower()}")
#         text_1 = text_1.replace(a,'_' + str(a.lower()))
# print(text_1)

# task 3

# dict_1 = {'C++':'Bjarne Stroustrup','Java':'James Gosling','Python':'Guido van Rossum','Pascal':'Niklaus Wirth'}
# c = dict_1['C++']
# j = dict_1['Java']
# p = dict_1['Python']
# pa = dict_1['Pascal']
# if 'C++' in dict_1.keys():
#     print('My favorite programming language is C++. It was created by', c)
# if 'Java' in dict_1.keys():
#     print('My favorite programming language is Java. It was created by', j)
# if 'Python' in dict_1.keys():
#     print('My favorite programming language is Python. It was created by', p)
# if 'Pascal' in dict_1.keys():
#     print('My favorite programming language is Python. It was created by', pa)
# dict_1.popitem()
# print(dict_1)

# task 4

# names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# n = str(names)
# delete_names = None, 32
# for n in names:
#   if n in delete_names:
#      continue
#   print(n)

# 5 task

# types = [1, 1000, 2, 12, {'key': 'value'}]
#
# for num in types:
#     if type(num) is int:
#         print(num)
#     else:
#       break
# for word in types:
#     if type(word) is dict:
#      print(f'цикл не працює з {type(word)} типом даних')


# task 6
#
#
# text = input('Enter characters: ')
# d = {}
# for i in text:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

