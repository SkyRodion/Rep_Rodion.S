# task 1 Palindrome

word = str(input("Введить слово: "))
back_word = word[:: -1]
if word == back_word:
    print('+')
else: print('-')

# task 2 text and word

text = str.casefold(input("Введить текст: "))
word = str.casefold(input("Введить слово: "))
text2 = text.split(' ')
if word in text2:
    print('Yes')
else: print('No')

# task 3 email
email = input("Введить email: ")
email_list = list(email)
if '@' and '_' in email_list:
    print('Yes')
else: print('No')

# #task 4

text = input("Введить текст: ")
text_2 = text.split()
if len(text_2) < 3:
    print('Кількість елементів менша за 3. Кількість елементів поточного списку: ', len(text_2))
else:
    print(text_2[-3:])








