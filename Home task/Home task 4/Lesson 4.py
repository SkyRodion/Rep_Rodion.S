# task 1

# list_1 = ["john", "marta", "james", "amanda", "marianna"]
# text_1 =' '.join(list_1)
# for i in text_1.split():
#    print(i.capitalize())

# task 2

list_1 = ["FirstItem", "FriendsList", "MyTuple"]

Fi = str(list_1[0])
Fi = Fi[0].lower() + Fi[1:]
Fr = str(list_1[1])
Fr = Fr[0].lower() + Fr[1:]
My = str(list_1[2])
My = My[0].lower() + My[1:]
for a in Fi:
    if a.isupper():
         Fi = Fi.replace(a, f"_{a.lower()}")
         print(Fi)
for a in Fr:
    if a.isupper():
        Fr = Fr.replace(a,    f"_{a.lower()}")
        print(Fr)
for a in My:
    if a.isupper():
         My = My.replace(a, f"_{a.lower()}")
         print(My)

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
# names_2 = [x for x in names if type(x) != type(None) if type(x) != int]
# print(names_2)
#
# for n in names:
#   if type(n) != type(None) and type(n) != int:
#    print(n)

# 5 task

# types = [1, 1000, 2, 12, {'key': 'value'}]
#
# for num in types:
#     if type(num) is int:
#         print(num)
#         continue
#     else: type(num) is dict
#     print(f'цикл не працює з {type(num)} типом даних')
#     break

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

