users = [
    {'name' : 'ali1', 'age': 21, 'city': 'tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'rasht'},
]

# function to get names by age:

def get_name_by_age(a):
    for item in users:
        if item['age'] == a:
            print(item['name'])
            break
    else:
        print('can not find')

get_name_by_age(24)         #--->  ali4
get_name_by_age(30)         #--->   'can not find'

#-------------------

# number of user in users:

print(len(users))           #------> 5

# -------------------

# to print data line by line: [ali1 - 21 - tehran]

def show_users(li):
    for item in li:
        for v in item.values():
            print(v, end=' - ')
        print()
show_users(users)

# or:

def show_users(li):
    for item in li:
        values = list(item.values())
        for i, v in enumerate(values):
            end_char = " - " if i < len(values) - 1 else ""
            print(v, end=end_char)
        print()

show_users(users)

#------------------------------------

# goal = remove the age, add birthday year. output ---> ['ali1 - tehran - 2004]

user = {'name': 'ali4', 'age': 24, 'city': 'tehran'}

user.pop('age')
user.update({'birthday' : 2004})

print(list(user.values()))

# ----------------------------------

# a function that removes age, and adds birthday:

def show_users(li):
        for item in li:
            values = list(item.values())
            for i, v in enumerate(values):
                end_char = " - " if i < len(values) - 1 else ""
                print(v, end=end_char)
            print()

def add_birthday():
    for user in users:
        user.update({'birthday': 2025 - user.get('age')})
        user.pop('age')
    show_users(users)

add_birthday()

#--------------------------------------

def func(x):
    return x ** 2
print(func(2))      # just shows the result

# or

res = func(2)
print(res)          # put the data into a variable, so you can use it later.

#--------------------------------------

y = lambda x: x ** 2
print(y(3))

#--------------------------------------

users = [
    {'name' : 'ali1', 'age': 21, 'city': 'tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'rasht'},
]

res = list(map(lambda item: item.get('name'), users))
print(res)

# or

res = map(lambda item: item.get('name'), users)
print(list(res))

#---------------------------------------------

result = map(lambda item: item.get('name'), users)
y = list(result).copy()

print(y)

