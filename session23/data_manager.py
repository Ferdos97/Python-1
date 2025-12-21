import json

class DataManager:
    def __init__(self, path = 'data.json'):
        self.path = path
        
    def get(self):
        with open(self.path, 'r') as f:
            return json.load(f)
    
    def set(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f)
