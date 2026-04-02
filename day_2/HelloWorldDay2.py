print("Hello, World!")
print(len("Hello, World!"))
print(type("Hello, World!"))
print(str(10))
print(int("10"))
print(float(10))
print("enter your name:")
print()
print(min(20,30,40,50))
print(max(20,30,40,50))
print(min([20, 30,40,50]))
print(sum([20, 30,40,50]))
print()
first_name, last_name, country, city, age, is_married = 'Byron', 'Espinoza', 'USA', 'Houston', 37, True 

skills = ["coding", "guitar", "IT"]
person_info =  {"car": "Kia Optima"}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name = input("What is your name: ")
age = input("How old are you? ")

print(first_name)
print(age)
print()
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0
print()
# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h'] 