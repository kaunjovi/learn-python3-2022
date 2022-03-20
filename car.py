class Car : 

    def __init__(self, name) : 
        print(f"Hello from constructor or init of car")
        self.name = name 

    def instance_hello(self) : 
        print(f"Hello from car {self.name}")

    def static_hello() : 
        print(f"Hello world from static method.")
        # This will not work. Static, cant access self
        # print(f"Hello world from static method {self.name}.")

    def count_of_wheels(self): 
        return 5 


# This is creating a car? without calling constructor
coupe = Car
# xuv.instance_hello() # xuv cant call instance methods
coupe.static_hello()           

# Call the Car() contructor to create an object 
maruti = Car("800")      ## maruti is an instance 
maruti.instance_hello()
print(f"# of wheels {maruti.count_of_wheels()}")
# maruti.static_hello() # instance cant call the static method



