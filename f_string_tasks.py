# |==========|==========|
# |         1|1         |
# |        23|23        |
# |       456|456       |
# |==========|==========|

# Not able to do it(

# ---------------------------------- Task 1 ---------------------------------- #
### Description:
#  Alice is 30 years old and her favorite color is black. Your task is to
#  store that information into variables and to print a greeting from Alice in
#  the console "Hello, my name is Alice, I am 30 years old, and my favorite color is black"
#  using the variables.

### Given:
name = 'Alice'
age = 30
color = 'black'

print(f"Hello, my name is {name}, I am {age} years old and my favorite color is {color}.")


### Expected output
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.

# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Create two numeric variables representing the year Alice was born and the current year.
#  Calculate Alice's age using these variables and an f-string, then print the result.

# ### Given:
# birth_year = 1993
# current_year = 2023

# age = current_year - birth_year

# print(f"Alice, your age is {age}")


### Expected output
# Alice is 30 years old.

# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Format the following number 1234567.89 to be displayed as a currency with two decimal places.
#  Example: "$1,234,567.89". Use an f-string to format and print the result.

### Given:
# amount = 1234567.89

# print(f"${amount:,.2f}")

### Expected output
#$1,234,567.89

# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Create a simple receipt format for the given shopping list items.
#  Use f-strings to format each item name aligned to the left and its price
#  aligned to the right. Each line should be 30 characters wide.

### Given:
item1_name = "Milk"
item1_price = 1.99

item2_name = "Bread"
item2_price = 2.49

item3_name = "Eggs"
item3_price = 3.59

print(f"{item1_name:30}{item1_price:.2f}")
print(f"{item2_name:30}{item2_price:.2f}")
print(f"{item3_name:30}{item3_price:.2f}")


### Expected output
# Milk                           1.99
# Bread                          2.49
# Eggs                           3.59

# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Alice is participating in a running marathon. She ran 42.195 kilometers in 3 hours, 45 minutes, and 30 seconds.
#  Calculate her average pace (minutes per kilometer) and total time in hours and print them using f-strings.
#  Format the pace to two decimal places.

### Given:
distance_km = 42.195
hours = 3
minutes = 45
seconds = 30

total_time_in_minutes = hours * 60 + minutes + seconds / 60
total_time_in_hours = total_time_in_minutes / 60
avarage_pace = total_time_in_minutes / distance_km


print(f"Alice your current performance is: {avarage_pace:.2f} min/km")
print(f"Your total time in hours is: {total_time_in_hours:.2f} h.")


### Expected output
# Alice's pace: 5.33 minutes/km
# Total time: 3.75 hours