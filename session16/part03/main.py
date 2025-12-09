import json

users = [
    {'name' : 'ali1', 'age': 21, 'city': 'tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'rasht'},
]

path = 'session16/part03/users.json'

with open(path, 'w') as f:
    json.dump(users, f)
