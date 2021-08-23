import copy

class Car():
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometr = 0
    def say_odometr(self):
        print('Одометр: ' + str(self.odometr))
    def comeback(self):
        r = self.make + ' ' + self.model + ' ' + str(self.year)
        return r.title()
        
newcar1 = Car('audi', 'a4', 2016)
newcar1.odometr = 10
newcar1.say_odometr()
print(newcar1.comeback())
newcar2 = copy.copy(newcar1)
newcar2 = Car('tesla', 'model s', 2016)
newcar2.odometr = 20
newcar2.say_odometr()
print(newcar2.comeback())