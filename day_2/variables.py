#Day 2 if python programming.
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "Byron", "Espinoza", "Byron Espinoza", "USA", "Houston", 37, 2026, True, True, False
print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(2026)
print(is_married)
print(is_light_on)
print()
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print()
print(len(first_name))
print(len(last_name))
num_one, num_two = 5, 4
print(num_one + num_two)
tot_num = num_one + num_two
print(tot_num)
print(num_two - num_one)
num_diff = num_two - num_one
print(num_diff)
num_prod = num_two * num_one
print(num_prod)
num_div = num_one / num_two
print(num_div)
num_rem = num_two % num_one
print(num_rem)
num_exp = num_one ** num_two
print(num_exp)
num_floor = num_one // num_two
print(num_floor)

import math
radius = 30

area_of_circle = math.pi * (radius ** 2)
print(area_of_circle)

circum_of_circle = (math.pi * radius) * 2
print(circum_of_circle)
user_radius = int(input("Enter Radius: "))
user_area = math.pi * (user_radius ** 2)
print(user_area)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
u_first_name = input("Enter First Name: ")
u_last_name = input("Enter Last Name: ")
u_country = input("Enter Country: ")
u_age = input("Enter Age: ")
print(f"I am {u_first_name} {u_last_name} I am from the {u_country} and I'm {u_age} years old!")