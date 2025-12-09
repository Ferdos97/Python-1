
import json

def get_data():
    with open('session19/data.json', 'r') as f:
        return json.load(f)

def set_data(Tasks):
    with open('session19/data.json', 'w') as f:
        json.dump(Tasks, f)
