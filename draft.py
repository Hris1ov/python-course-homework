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

# 'Hello, Adam Byron!'
# print( f'''
# Hello,\n\n{user_name} {user_surname}\n\n{signature}
# '''
# )

# x = 123
# print(f"-->{x:>10}<--")
# print(f"-{x:<30.2f}")

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

# print('''
# This is a random text with \"quotes\" in some places.\n
#     For example, here is a sentence with a \"quote\" in the middle.\n\t
#     Let's also add a new tab here for indentation.\n
# This line contains a \"quote\" and we want to add a new line.\n
# Here comes another quote: \"Be yourself; everyone else is already taken.\"\n
# Finally, let's end with a new line and a tab:\n	
# 	\t\"End of example.\"
# ''')



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
    


#--------------------------- List comprehensions ---------------------------------

# new_list = [expression for item in iterable if condition]

# expression – какво ще бъде добавено в new_list
# item – текущият елемент от iterable (например списък, диапазон, низ и др.)
# iterable – последователност от елементи, през които преминаваме
# condition (по желание) – филтър, който определя дали даден елемент ще бъде включен в new_list

# Напиши програма, която създава списък с квадратите на числата от 1 до 20 с помощта на list comprehension.

# squares = [number**2 for number in range(1,21)]
# print(squares)

# Очакван резултат:

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

# Филтриране на нечетните числа
# Създай списък, който съдържа само нечетните числа от 1 до 20.

# odds = [num for num in range(1,21) if num%2!=0]
# print(odds)

# Напиши програма, която взема списък от думи и връща списък с дължините им.

# words = ["python", "code", "list", "comprehension", "exercise"]

# word_len = [len(words) for words in words]
# print(word_len)

#--------------------------- Functions ---------------------------------

# def increment(number, by=1, ):
#     return number + by

# print(increment(2+0))

# def hello_func(greet):
#     return '{} function'.format(greet)

# print(hello_func('Hi'))

# def greet(name):
# #    input(f"Please enter a name: ")
#     print(f"Hello, {name}!")

# greet('Alice')

# def plus(a,b):
#     return a + b

# print(plus(2,3))

# def plus(a,b):
#     return a + b

# print(plus(2,3))

# def aver(*numbers):
#     return sum(numbers) / len(numbers)

# print(f"{aver(1,2,3,4,5):.2f}")

# def greet(name="Please enter your name"):
#     print(f"Hello, {name}!")

# greet()

# def add(a, b):
#     return a + b

# print(add(3, 5))

# def is_even(n):
#     return n % 2 == 0

# print(is_even(int(input("Enter a number: "))))

# def reverse_string(string):
#     return string[::-1]

# input = (str(input("Enter a string: ")))
# print(reverse_string(input))

# def max_number(*numbers):
#     return max(numbers)

# print(max_number(1,2,3,4,5))

# def system(**kwargs):
#     print("System Information:"
#     "\n")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# system(Software='MacOS', Version='18.01', Memory='48GB', Storage='2TB')

# def individual(version, name = 'wifi'):
#     print(f"This is a special {name} version {version}.")

# individual("handsfree")

# def foo(*fruits):
#     print(fruits)

# foo('apple', 'banana', 'cherry')

# Define the calculate_sum() function, which will print the sum of variable number of numerical arguments
#  # calculate_sum() definition

# # test your code:
# calculate_sum(1)
# #should print 1

# calculate_sum(1,2)
# #should print 3

# calculate_sum(1,2,3)
# #should print 6

# def calculate_sum():
#     return sum(range(1,6))

# print(calculate_sum())

# def menu_print(fruit, price):
#     print(f"{fruit:.<20s}{price:.2f}")

# menu_print("apple", 2.50)

# def outer():
#     x = 2

#     def inner():
#         x = 3
#         print(f"x = {x} in inner")

#     inner()
#     print(f"x = {x} in outer")

# x = 1
# outer()
# print(f"x = {x} in global")

#--------------------------- *args ---------------------------------

# def simple(first_name, *args):
#     print(f"Hello, {first_name}")
#     for others in args:
#         print(f"Bye, bye {others}")

# simple("Bob", "Moby", "Foggy")

# def filter_even(*args):
#     even_nums = []
#     for num in args:
#         if num % 2 == 0:
#             even_nums.append(num)
#     return even_nums

# print(filter_even(1, 2, 3, 4, 5, 6))

# def find_max(*args):
#     for arg in args:
#         return max(args)
    

# print(find_max(10, 22, 5, 17))  

# import statistics

# def average(*args):
#     return mean(args)

# print(average(4, 8, 6))  

from statistics import mean

def sum_average(*args):
    return sum(args), mean(args), min(args)

print(sum_average(5, 10, 15))  



#--------------------------- Lambda ---------------------------------

#--------------------------- Map ---------------------------------

#--------------------------- OOP ---------------------------------

# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def greet(self):
#        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# p1 = Person("Alice", 25)
# p1.greet()

# class Car:
#     def __init__(self,brand: str,speed: int):
#         self.brand = brand
#         self.speed = speed

#     def accelarate(self,amount):
#         self.speed += amount

# car = Car("BMW",200)
# car.accelarate(20)
# print(car.speed)

# Направи клас Animal с метод make_sound(), който връща "Some sound".
# Създай клас Dog, който наследява Animal, но методът make_sound() връща "Woof!".

# class Animal:
#     def __init__(self,animal):
#         self.animal = animal
    
#     def make_sound(self):
#         return f"There is no sound for {self.animal}"
    
# class Dog(Animal):
#     def make_sound(self):
#         print( "Woof")

# class Cat(Animal):
#     def sleep(self):
#         pass

# # dog = Dog("Dog")
# cat = Cat("Cat")

# print(cat.make_sound())

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

# class Triangle(Shape):
#     def __init__(self, color, is_filled, height):
#         super().__init__(color, is_filled)
#         self.height = height

# class Square(Shape):
#     def __init__(self, color, is_filled, side):
#         super().__init__(color, is_filled)
#         self.side = side

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

# tr = Triangle("red", True, 5)
# sq = Square("blue", False, 4)
# cr = Circle("green", True, 3)

# print(f"Triangle color: {tr.color}, height: {tr.height}")
# print(f"Square color: {sq.color}, side: {sq.side}")
# print(f"Circle color: {cr.color}, radius: {cr.radius}")

# class Car:
#     total = 0

#     def __init__(self, manufacturer):
#         self.manufacturer = manufacturer
#         Car.total += 1

#     @classmethod
#     def create_car(cls, manufacturer):
#         return cls(manufacturer)
    
# car1 = Car.create_car("Lian")
# car2 = Car.create_car("BYD")

# print(Car.total)

###

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello my name is {name} and I am {age} years old"
    
#     person1 = ("Scrolina", 26)
#     person2 = ("Spirolina", 21)

#     print(person1)

###

# class Book:
#     def __init__(self, tittle, author, year):
#         self.tittle = tittle 
#         self.author = author
#         self.year = year

#     def display_info(self):
#        return f"Book is {self.tittle}, written by {self.author} from {self.year} year."
    
# book1 = Book("Huba-Buba", "Hans-Christian Andersen", 1874)
# book2 = Book("Only I don't know Python", "me", 2025)

# print(book1.display_info())

###

# class Vehicle:
#     def move(self):
#         return f"This shit is mf movingf"

# class Car(Vehicle):
#     def move(self):
#         return f"This $h#t is moving."

# class Bike(Vehicle):
#     def move(self):
#         return f"This thing is flying my head."

# car = Car()
# print(car.move())
# bike = Bike()
# print(bike.move())

###

# class Animal:
#     def __init__(self):
#         pass
    
#     def make_sound(self):
#         pass

# class Dog:
#     def make_sound(self):
#         return f"This fluffy is woofing at me."
    
# class Cat:
#     def make_sound(seld):
#         return f"The little cat is meowing all day around the house."

# dog = Dog()
# print(dog.make_sound())   
# cat = Cat()
# print(cat.make_sound())

###

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
    
#     def deposit(self, amount):
#         self.__balance += amount
#         return f"You are not rich but you now have {self.__balance}."

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return f"Sorry brokie"
#         else:
#             self.__balance -= amount
#             return f"You still have {self.__balance}."
        
#     def get_balance(self):
#         return self.__balance

# account1 = Account("John Doe", 1000)
# # account1.deposit(500)
# # account1.withdraw(3000)
# print(account1.deposit(200))
        
###

# class MathUtils:

#     @staticmethod
#     def multiply(a, b):
#         return a * b

# print(MathUtils.multiply(6, 3))

# ###

# class Person:
#     def __init__(self, population)
#         self.population = population

#     @classmethod
#     def get_population(cls):
#         return cls.population
    
###

# class Shapes:

#     def __init__(self):
#         pass

#     def rectangle(self, height, width):
#         self._height = height
#         self._width = width

#     @property
#     def height(self):
#         return f"Height is {self._height:.2f} cm"
    
#     @property
#     def width(self):
#         return f"Width is {self._width:.2f}cm"
    
# rect = Shapes()
# rect.rectangle(3.6, 5.2)
# print(rect.height)
# print(rect.width)

#---------------------------- Iterators ---------------------------------

# names = [
    
#     "Ivan", "Maria", "Gosho"
    
#     ]

# class NameIterator:
#     def __init__(self, names):
#         self.names = names
#         self.index = 0

# def __iter__(self):
#     return self

# def __next__(self):
#     for name in names:
#         name += 1
#         return name
#     raise StopIteration

# names = iter(names)
# print(next(names))
# print(next(names))
# print(next(names))

# echo = str("Hello, world!")
# iterator = iter(echo)
# print(next(iterator))  # H
# print(next(iterator))  # e
# print(next(iterator))  # l
# print(next(iterator))  # l
# print(next(iterator))  # o
# print(next(iterator))  # ,
# print(next(iterator))  #
# print(next(iterator))  #
# print(next(iterator))  # w
# print(next(iterator))  # o
# print(next(iterator))  # r
# print(next(iterator))  # l
# print(next(iterator))  # d

# class Evens:
#     def __init__(self, number):
#         self.number = number
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.index < len(self.number):
#             result = self.number[self.index]
#             self.index += 1
#             if result % 2 == 0:
#                 return result
#         else:
#             raise StopIteration
        
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = Evens(numbers)
# for n in evens:
#     print(n)

# class RepeatWord:
#     def __init__(self, word, times):
#         self.word = word
#         self.times = times
#         self.count = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count < self.times:
#             self.count += 1
#             return self.word
#         else:
#             raise StopIteration

# Задача 1: Основен итератор с iter() и next()

# Задача:
# Имаш списък: numbers = [10, 20, 30].

# Създай итератор.
# Използвай next() три пъти, за да отпечаташ елементите.


# class ThreeIterator:
#     def __iter__(self):
#         return self
    
#     def __next__(self)

#---------------------------- Imports ---------------------------------

# import os

# file_path = "tmp.py"

# if os.path.exists(file_path):
#     print(f"{file_path} exists")
# else:
#     print(f"{file_path} does not exist")

# class NumberIterator:
#     def __init__(self, num):
#         self.num = num
#         self.current = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.num:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
    
# num_iterator = NumberIterator(6)

# for value in num_iterator:
#     print(value)

# class UpIterator:
#     def __init__(self, word):
#         self.word = word
#         self.current = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.current < len(self.word):
#             character = self.word[self.current]
#             self.current += 1
#             if character.isupper():
#                 return character
#         raise StopIteration
        
# for char in UpIterator("HeLlo PythOn"):
#     print(char)

