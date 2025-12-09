users = [
    {'name': 'ali1', 'age': 21, 'city': 'tehran'},
    {'name': 'ali2', 'age': 22, 'city': 'tehran'},
    {'name': 'ali3', 'age': 23, 'city': 'karaj'},
    {'name': 'ali4', 'age': 24, 'city': 'tehran'},
    {'name': 'ali5', 'age': 25, 'city': 'rasht'},
]

# list comprehension: here we use it to create a new list from a iterator.

names = [item.get('name') for item in users]
print(names)

# output: --------> ['ali1', 'ali2', 'ali3', 'ali4', 'ali5']

# -------------------------------------------

# map: get or create a value from iterator:

m = map(lambda item: item.get('name'), users)
print(list(m))

# --------------------------------------------

# filter : who is from Tehran?

f = filter(lambda item: item.get('city') == 'tehran', users)
print(list(f))

# ------------------------------------

# whose age is more than 23?

f2 = filter(lambda item: item.get('age') > 23, users)
print(list(f2))

#---------------------------------------

# a list for names of user who are from tehran:

f3 = filter(lambda item: item.get('city') == 'tehran', users)
m = map(lambda item: item.get('name'), f3)
print(list(m))

# output -------------> ['ali1', 'ali2', 'ali4']

# --------------------------------------

m = map(lambda item: item.get('name'),
        filter(lambda item: item.get('city') == 'tehran', users)
        )

m = (list(m)).copy()
print(m)
print(m)
print(m)

# ----------------------------------------------

# sorted:

li = ['a' , 's', 'z', 'b']
li.sort()
print(li)
# output -------------> ['a', 'b', 's', 'z']

#-------------------------------------------------

li.sort(reverse=True)
print(li)

#output --------------> ['z', 's', 'b', 'a']

# ------------------------------------------------

s = sorted(users, key=lambda item: item.get('city'))
print(s)

# sorts dict items by cities: karaj , rasht, tehran

## or

m = map(lambda item: item.get('name'),
        sorted(users, key=lambda item: item.get('city'))
        )

print(list(m))

## sorts people names by their city names.
## output ----> ['ali3', 'ali5', 'ali1', 'ali2', 'ali4']

# --------------------------------------------------