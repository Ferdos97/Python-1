
# Class ===> blueprint
# Object ==> instance of class
# Method ==> function
# Property ==> variable

class Car:
    # def __init__(self, *args):
    #     print('args: ', args)

    def __init__(self, name, model, company, color):
        print(color)
        self.name = name
        self.color = color
        self.model = model
        self.company = company
        self.speed = 10

    def show_info(self):
        print(self.name, self.color, self.model)

    def go_faster(self):
        self.speed += 10
        print(self.speed)

    def go_slower(self):
        self.speed -= 10
        print(self.speed)


machine206 = Car('206', 2025, 'Peugeot', 'blue')
machine207 = Car('207', 2023, 'Peugeot', 'blue')

machine206.show_info()
machine207.show_info()


machine206.go_faster() # +10
machine206.go_faster() # +10
machine206.go_faster() # +10
machine206.go_faster() # +10

machine207.show_info()