
# Create venv:
# python -m venv .venv


# Get the source of python:
# which python
# python --version


# Activate venv in terminal:
# source .venv/Scrpits/active
# deactivate


# PIP = Package Manager:

# pip install camelcase
# pip uninstall camelcase
# pip freeze
# pip freeze > requirements.txt
# pip install -r requirements.txt

#---------------------------------------

import re

text = 'the rain in spain has started 9pm, feels like pain'


pattern = 'in'
result = re.findall(pattern, text)
print(result)


pattern = ' in '
result = re.findall(pattern, text)
print(result)

#------------------------------------

text = 'the rain in spain has started 9pm, feels like sin'

pattern = r'\win\s'
result = re.findall(pattern, text)
print(result)


pattern = r'\d[ap]m'
result = re.findall(pattern, text)
print(result)


pattern = r'^t'
result = re.findall(pattern, text)
print(result)


pattern = r'\s\w*in'
result = re.findall(pattern, text)
print(result)


pattern = r'\s\w*in\s'
result = re.findall(pattern, text)
print(result)
