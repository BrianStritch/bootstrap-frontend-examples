from run import max_guests

# create the class template basically


class Person:
    def __init__(self, age, weight, height, first_name, last_name, hair_color):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.hair_color = hair_color
    
    def singing(self):
        print('is singing')

    def dancing(self):
        print('is dancing')
    


class Car:
    def __init__(self, make, model, fuel, engine_size, reg):
        self.make = make
        self.model = model
        self.fuel = fuel
        self.engine_size = engine_size
        self.reg = reg

    def driving(self):
        print('is driving along in my car')
    
    def parked(self):
        print('is now parked')



# how to create an instance of my classes above

darcy = Person(6, '2kg', '3.6ft', 'Darcy', 'Stritch', 'Blonde')


silvia = Car('nissan', 'silvia', 'petrol', '1.8', '86l445')

print(darcy.first_name)
darcy.singing()

print(darcy.first_name)
silvia.driving()