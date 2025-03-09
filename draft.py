#--------------------   Booleans   --------------------

# x = 5
# x += 3
# print(x)

# x = 5
# x = x + 3
# x = 5 + 3 = 8

# fruits = ("intel","silicone","amd")

# if "silicone" in fruits:
#     print("Silicone is in fruits")


#--------------------   Format F strings   --------------------

#   print( '2+2',{Adam})

# user_name = 'Adam'
# user_surname = 'Byron'
# signature = 'Best regards,'

# #'Hello, Adam Byron!'
# print( f'''Hello,\n{user_name} {user_surname}|\n\n
# \t{signature}''')

# x = 123
# print(f"-->{x:>10}<--")
# print(f"-{x:<30.2f}-")

# Въведете вашето име: Иван
# Въведете вашата възраст: 30

# name = input("Please enter your name:")
# age = input("Please enter your age:")
# print(f"Your name is: {name}")
# print(f"Your age is: {age}")

# number = (float(input("Please enter a number:")))
# print(f"Your number in percentage is: {number:.4%}")

# length_of_rectangle = int(input("Please enter the lenght: "))
# width_of_rectangle = float(input("Please enter the width: "))

# area = length_of_rectangle*width_of_rectangle

# print(f"P = {area:.3f}")

# F = C*(9//5)+32

# celsius = int(input("Please enter Celsius temperature: "))
# farenheit = celsius*9/5+32

# print(f"The Farenheit temparature is {farenheit:.2f}")

# date = int(input("Please enter a day of the month: "))
# month = int(input("Please enter a month: "))
# year = int(input("Please enter year: "))

# print(f"Your date is: {date:02}/{month:02}/{year:04}")



# ================== Homework =======================

# print(1,2,3,sep="-")

# print("Hello",end="")
# print("World",end="")
# print("!")

# x = 3
# print(type(x==3))

# name = input("Enter your name: ")
# print(f"Hello, {name}!")
# age = input("Tell me your age:")
# print(f"Ok, you look younger than {age}")


# print('12'>'18')

# print("-"*20," ","Escape Sequences"," ","-"*20)

#--------------------   Escape Sequences   --------------------

# print('lego1\nlego2')

# print('Distance\tmatters')
# print('Distance         matters')

# print('Shakespeare always told his friends about \"his great brown horse\"')

# print('''This is a random text with \"quotes\" in some places.\n
#     For example, here is a sentence with a \"quote\" in the middle.\n\t
#     Let's also add a new tab here for indentation.\n
# This line contains a \"quote\" and we want to add a new line.\n
# Here comes another quote: \"Be yourself; everyone else is already taken.\"\n
# Finally, let's end with a new line and a tab:\n	
# 	\t\"End of example.\"''')



# text = '''This is a random text with \"quotes\" in some places.\n
#     For example, here is a sentence with a \"quote\" in the middle.\n\t
#     Let's also add a new tab here for indentation.\n
# This line contains a \"quote\" and we want to add a new line.\n
# Here comes another quote: \"Be yourself; everyone else is already taken.\"\n
# Finally, let's end with a new line and a tab:\n	
# 	\t\"End of example.\"'''
# print(text.strip().title())

# text = '''This is a random text with \"quotes\" in some places.\n
#     For example, here is a sentence with a \"quote\" in the middle.\n\t
#     Let's also add a new tab here for indentation.\n
# This line contains a \"quote\" and we want to add a new line.\n
# Here comes another quote: \"Be yourself; everyone else is already taken.\"\n
# Finally, let's end with a new line and a tab:\n	
# 	\t\"End of example.\"'''
# print(text.upper())

#--------------------   Counting   --------------------

# count_t = text.count("t")
# print(f"The letter 'T' appears: {count_t} times in the text.")

# count_newlines = text.count('\n')
# print(f"The newline appears: {count_newlines} times in the text.")

#-------------------- Conditions ----------------------

# if 2+2:
#     print('hi')
#     print('Howdy')

# Interpolating 5 to x. If module of x is equal to 0 print of odd
# x = 5

# if x%2 == 2:
#     print('Odd')
# else:
#     print('Even')

# usr_lg = 'IT'

# if usr_lg == 'IT':
#     print('Ciao')
# elif usr_lg == 'BG':
#     print('Здравейте')
# else:
#     print('Hello')

#-------------------- Sequences --------------------

# Sequence - последователност. List, Tuple, Range, String

# Типовете данни за последователности са основна концепция, обхващаща няколко вградени типа, използвани за съхраняване на колекции от данни.  
# Разбирането на тези типове е ключово за изпълнението на широк спектър от задачи в Python – от манипулация на данни до използване на цикли.  
# Последователността в Python е контейнер, който съхранява подредена колекция от обекти.  
# Основните типове последователности са **списък (list), кортеж (tuple), диапазон (range) и низ (string).
# Всяка последователност има индекс - i, като се брой от 0. Независимо от типа Sequence, всички използват операциите: length, indexing, 
# slicing, concatenation, repetition, membership test, min, max, count, index.

#-------------------- List --------------------

# mutable sequence

# list1 = ["cat","dog","banana"]
# print(list1[-2])

# mylist = ["nothing", 1, "anything"]
# print(type(mylist))
# print(mylist)
# print(f"Your list contains: {mylist[1]:>30} thing")
# print(len(mylist))

# fruits = ['apple','banana','cherry','ants']
# fruits.append('melon')
# print(fruits)
# fruits.sort()
# print(fruits)

# Създай списък с числата от 1 до 10 и принтирай само първите 5 числа.
# 2️⃣ Добави елемент "Python" в края на списъка ["Java", "C++", "JavaScript"].
# 3️⃣ Замени третия елемент в списъка [10, 20, 30, 40, 50] с "Hello".
# 4️⃣ Преброй колко пъти числото 5 се среща в [5, 1, 5, 2, 5, 3, 5].
# 5️⃣ Изтрий всички четни числа от [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[0][1][2][3][4])

# program_languages = ["Java", "C++", "JavaScript"]
# program_languages.append["Python"]
# print(program_languages)

# list_replace = [10, 20, 30, 40, 50]
# list_replace[2] = "Hello"
# print(list_replace)


#-------------------------  Tuple  ---------------------------

# imutable sequence

# user_birth_date = ("24","September",1992)
# print(f"You are born on {user_birth_date[1]}")

# tuple1 = ("thing","another thing","melon")
# list_from_tuple = list(tuple1)
# list_from_tuple[1] = ("choco")
# tuple1 = tuple(list_from_tuple)
# print(tuple1)

# fruits_as_a_tuple = ("apple", "banana", "cherry")
# list_from_tuple = list(fruits_as_a_tuple)
# list_from_tuple[0] = "milk"
# other_tuple_from_fruits = (list_from_tuple)
# print(other_tuple_from_fruits)

# # Define tuple
# monitoring = ("dynatrace","grafana","sitescope")
# # List the tuple
# l_monitoring = list(monitoring)
# # Modify the list by append
# l_monitoring.append("banana")
# # Define new tuple with modified list 
# tuple_l_monitoring = tuple(l_monitoring)
# # Print the new tuple
# print(tuple_l_monitoring)

# numbers = (10, 20, 30, 40, 50)
# lnumbers = list(numbers)
# lnumbers.remove(40)
# new_numbers = tuple(lnumbers)
# print(new_numbers)

# Increment with 10 all the numbers in the tuple

# nums = (1,2,3,4,5,6)
# l_num = list(nums)
# l_num = [x + 10 for x in l_num]
# t_num = tuple(l_num)
# print(t_num)

# Add element in tuple by list

# colors = ("red","green","blue","yellow")
# list_colors = list(colors)
# list_colors.append("orange")
# new_colors = tuple(list_colors)
# print(new_colors)

# Remove element from tuple by list

# elements = ("carbon", "ceramic", "plastic")
# list = list(elements)
# del list[1] # here you remove the number of element from the list
# refined = tuple(list)
# print(refined)

# elements = (1,2,3,4)
# list = list(elements)
# list.remove(2) # here you remove the exact element from the list
# new_elements = tuple(list)
# print(new_elements)

# elements = (1,2,3,4)
# list = list(elements)
# list = [x * 10 for x in list]
# new_elements = tuple(list)
# print(new_elements)

# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[-2:])


# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# fruits = (["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"])
# fruits.append("eagle")
# print(fruits)

# 6️⃣ Създай кортеж от 5 имена и вземи последните 3.

# names = ("al","bl","vl","gl","meh")
# print(names[-3:])

# 7️⃣ Провери дали числото 50 е в кортежа (10, 20, 30, 40, 50).

# num = (10, 20, 30, 40, 50)
# print(50 in num)

# 8️⃣ Обедини два кортежа (1, 2, 3) и (4, 5, 6) в нов.

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# merged = tuple1 + tuple2
# print(merged)

# 9️⃣ Конвертирай кортежа ("a", "b", "c") в списък, добави "d", и го върни обратно в кортеж.

# gtuple = ("a", "b", "c")
# elist = list(gtuple)
# elist.append("d")
# tuple1 = tuple(elist)
# print(tuple1)

# 🔟 Извади елемент от кортеж чрез индекса му, например, вземи третия елемент от ("apple", "banana", "cherry", "date").


# my_tuple = ("apple", "banana", "cherry", "date")
# my_list = list(my_tuple)
# del my_list[-2]
# my_new_tuple = tuple(my_list)
# print(my_new_tuple)




#--------------------------- Range ---------------------------------

# imutable sequence

import sys
# things = range(1,23356,2)
# print(list(things))
# print(f"{sys.getsizeof(things)}")

# numbers = list(range(1, 6))
# print(type(numbers))

# user_names = []

# for _ in range(5):
#     user_name = input('Your name: ')
#     user_names.append(user_name)

# print(user_names)

# numbers = range(1,11)
# print(list(numbers))

# odd = range(2,22,2)
# print(list(numbers))

# reverse = range(10,0,-1)
# print(list(reverse))

# five = range(5,55,5)
# print(list(five))

# for я in range(1, 11):
#     print(f"7 x {я} = {7 * я}")

# for number in range(5):
#     print(list(number))

# 1️⃣1️⃣ Създай range от 1 до 20 и го превърни в списък.

# smtg = range(1,21)
# my_list = list(smtg)
# print(my_list)

# 1️⃣2️⃣ Принтирай всички четни числа между 1 и 50, използвайки range().

# even = list(range(2,52,2))
# print(odd)

# 1️⃣3️⃣ Принтирай числата от 100 до 50, използвайки range() със стъпка -5.

# myrange = list(range(100,49,-5))
# print(myrange)

#--------------------------- Slicing ---------------------------------

# text = [1,2,3,4,5,6,7,8,9,10]
# # print(text[1:9:2])

# for i in list(text):
#     print(text[::2])

# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[:3])

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(fruits[-2:])

# my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
# mylist = list(my_tuple)
# print(mylist[1:4])

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# mylist = list(numbers)
# print(mylist[::2])

# text = "Hello, world!"
# print(text[:5])

#--------------------------- for ---------------------------------


# fruits = ("apple", "banana", "cherry", "kiwi", "orange")
# for i in fruits:
#     print(i)

# values = (5, 15, 25, 35, 45)
# total = 0
# for i in values:
#     total += i
#     print(total, end=" ")

# Използвай цикъл, за да намалиш стойността на x от 15 до 1, намалявайки с 2 при всяка стъпка. Принтирай резултата.

# value = 15
# while value > 0:
#     print(value, end=", " if value > 1 else "")
#     value -= 2
    
# Използвай цикъл, за да симулираш редуциране на парична стойност от 50 до 0, като при всяка стъпка намаляваш парите с 7. Ако парите са по-малко от 7, спри цикъла и покажи съобщение.

# money = 50

# while money > 7:
#     money -= 7
#     print(f"Current cash: {money}")


# if money <= 7:
#     print("Brokie.")

# Използвай цикъл, за да намалиш стойността на x от 25 до 0, намалявайки с 3 при всяка стъпка.

# x = 25

# while x > 0:
#     x -= 3
#     print(x, end=", ")

# Задача 1: Напиши програма, която започва с числото 100 и намалява с 5 на всяка итерация, докато не стане по-малко от или равно на 10. Използвай while цикъл, за да отпечатваш числата.

# program = 100

# while program >= 10:
#     print(program, end=", ")
#     program -= 5

# Задача 2: Напиши програма, която започва с числото 1 и умножава с 2 на всяка итерация, докато стойността не стане по-голяма от 100. Използвай while цикъл и отпечатвай всяко число.

# i = 1

# while i <= 100:
#     print(i, end=", ")
#     i *= 2

# Задача 3: Напиши програма, която започва с числото 0 и добавя 1 към числото на всяка итерация, докато числото стане равно на 10. Използвай while цикъл и отпечатвай числото на всяка стъпка.

# program = 0

# while program <= 10:
#     print(program, end=", ")
#     program += 1

# Задача 4: Напиши програма, която започва с числото 1 и на всяка стъпка увеличава числото с 1, докато стойността му не стане 20. Но отпечатвай само нечетни числа. Използвай while цикъл.

# z = 0

# while z <= 20:
#     if z % 2 == 0:
#         print(z, end=", ")
#     z += 1

# Задачи с for цикъл:
# Задача 5: Напиши програма, която използва for цикъл, за да отпечата всички числа от 1 до 50, които са кратни на 7.

# for number in range (1,51):
#     if number % 7 == 0:
#         print(number, end=", ")

# Задача 6: Напиши програма, която използва for цикъл и отпечатва всички елементи от списък: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], но ако числото е четно, отпечатвай "even", ако е нечетно - "odd".

# for number in range(1, 11):
#     if number % 2 != 0:
#         print(f"{number} is odd")
#     if number % 2 == 0:
#         print(f"{number} is even")

# Задача 7: Напиши програма, която използва for цикъл, за да изчисли сумата на всички числа от 1 до 100 и я отпечата.

# total = 0
# for x in range(1, 101):
#     total += x
#     print(total)

# Задача 8: Напиши програма, която използва for цикъл и отпечатва всички елементи от списък: fruits = ["apple", "banana", "cherry", "date"], но само ако дължината на елемента е по-голяма от 5.

# fruits = ["apple", "banana", "cherry", "date"]

# for fruit in fruits:
#     if len(fruit) > 5:
#         print(fruit)

# Задача 10: Напиши програма, която използва for цикъл и събира всички стойности от списък: values = [12, 24, 36, 48, 60], които са кратни на 12 и отпечатва резултата.

# values = [12, 24, 36, 48, 60]
# total = 0

# for element in values:
#     if element % 12 == 0:
#         total += element
# print(total)

# Използвай цикъл, за да намалиш стойността на x от 50 до 1, намалявайки с 5 при всяка стъпка. Принтирай резултата.

# x = 50

# while x > 0:
#     x -=5 
#     print (x, end=" ")

# 1️⃣ Сумиране на четни числа от 1 до 50:
# total = 0

# for num in range(1,51):
#     if num % 2 == 0:
#         total += num # total = total + num
# print(f"the sum is: {total}")

#--------------------------- Copy by reference/value ---------------------------------

# Copy by Reference	

# При mutable типове (list, dict, set), когато направим присвояване (b = a), двете променливи сочат към същия обект в паметта, затова копие по референция.
# Python прави това, за да пести памет. Промените в едната променлива засягат и другата.

# Copy by Value

# При immutable типове (int, bool, float, str, tuple), ако променим стойността, референцията се пренасочва към нов обект, затова е копие по стойност
# Старата стойност остава без референция и Garbage Collector (GC) може да я изтрие.

# Пример за immutable:
# a = 10
# b = 15
# print(id(a))  # ID на а (10)
# print(id(b))  # ID на b (15)

# b = 10  # Пренасочваме b към нов обект (10)
# print(id(b))  # ID на b вече е като на a

# # При mutable обекти, ако искаме да направим копие, което да НЕ засяга оригинала, използваме shallow copy (копиране на първото ниво) чрез метода copy().

# # Пример за shallow copy:
# a = [10]
# b = [15]
# b1 = b.copy()  # Създаваме нов списък с идентични стойности

# print(id(b))   # ID на оригиналния списък
# print(id(b1))  # ID на копието (различен от b)

# b1.append(6)  # Добавяме елемент към копието
# print(b)   # Оригиналът остава непроменен [15]
# print(b1)  # Копието е променено [15, 6]




#--------------------------- Membership test: in/not in ---------------------------------


#--------------------------- Dictionaries ---------------------------------

# Напиши програма, която създава речник със следните двойки ключ-стойност:

# "name": "Ivan"
# "age": 25
# "city": "Sofia"

# След това отпечатай името и възрастта.

# info = {
# "name": "Ivan",
# "age": 25,
# "city": "Sofia"
# }

# print(f"He is {info['name']} and he is {info['age']} yo.")


# fruits = {
#     'banana': 6.50,
#     'melon': 3.10,
#     'plums': 3.10
# }

# print(fruits['plum'])
# print(id(fruits['melon']))
# print(id(fruits['plums']))
# fruits['plum'] = 3.50
# print(id(fruits['plums ']))

# keys = fruits.keys()
# print(keys)

# val = fruits.values()
# print(val)

# Добавяне и премахване на елементи
# Задача:
# Създай речник със следните двойки:

# person = {"name": "Maria", "age": 30, "job": "engineer"}
# Добави нов ключ "salary" със стойност 3500.
# Изтрий ключа "job".
# Отпечатай обновения речник.

# person = {
#     "name": "Maria", 
#     "age": 30, 
#     "job": "engineer"}

# person['salary'] = 3500
# # print(person)

# del person['job']
# print(person)

# prices = {
#     "apple": 2.50, "banana": 1.80, "orange": 2.20, "grape": 3.00
#     }

# for fruit, price in prices.items():
#     print(f"The price of {fruit} is:  {price}")

# print(prices.keys())
# print(prices.values())
# print(prices.items())
# print(prices)

# Създай речник с информация за автомобил (марка, модел, година).
# Изведи стойността за ключа "марка".

# cars = {
#     'manufacturer': 'Ford',
#     'model': 'T',
#     'year': 1892

# }

# print(cars.values())

# cars_new = {
#     'manufacturer': 'Ford',
#     'model': 'F150',
#     'year': 1995

# }

# cars_summary = [cars, cars_new]
# print(cars_summary.sorted())

# cars_new = {
#     'manufacturer': 'Ford',
#     'model': 'F150',
#     'year': 1995
# }

# del cars_new['model']
# print(cars_new.items())

# words = ["ябълка", "банан", "портокал", "грозде"]
# word = words[::-1]

# for fr in word:
#     print(fr, end=",")
    
