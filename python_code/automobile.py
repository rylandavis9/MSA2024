#create an automobile class
#define a consturcter
#constructor is a function that executes when an object or  is created
class Automobile():
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign class properties values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year