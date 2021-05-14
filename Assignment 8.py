#Alex Hanna
#Assignment 8
#05/07/2021

class  Vehicle: #parent class initialized
     
    def __init__(self):
        
        self.make = input("Make of vehicle:")
        self.model = input("Model of vehicle:")
        self.color = input("Color of vehicle:")
        self.fuelType = input("Fuel Type:")
        self.options = ["power mirrors","power locks", "remote start",
        "backup camera", "bluetooth", "cruise control", "all wheel drive", "heated seats"]

        # class atrributes initialized

    def get_Make(self):
        return self.make
    
    def get_Model(self):
        
        return self.model
    
    def get_Color(self):
    
        return self.color

    def get_Fuel_Type(self):
        
        return self.fuelType

    def get_options(self):
        self.options = input(f"Select from the list of available options: {self.options} ") #lets user choose from list of available options
        return self.options
        
     
    # 5 functions defined and will return values from user input    

class Car(Vehicle):  # Child class Car 

    def __init__(self):
        Vehicle.__init__(self) # passes attribute values from parent class
        self.engineSize = input("Engine size of Car:")
        self.numDoors = input("Number of Car doors:")

    def get_Engine_Size(self):
        return self.engineSize

    def get_Num_Doors(self):
        return self.numDoors

    # 2 functions defined and will return two user input values 

class Pickup(Vehicle): # Child class Pickup

    def __init__(self):
        Vehicle.__init__(self) #passes attribute values from parent class
        self.CabStyle = input("Enter Engine Cab Style:")
        self.bedLength = input("Enter Bed Length:")

    def get_Cab_Style(self):
        return self.CabStyle

    def get_Bed_Length(self):
        return self.bedLength

prompt = ("Would you like to add a Car or Pickup? When finished enter done:")# prompts user to enter if they want a car or pickup
print()

while True: #while condition that will create prompt until user enters done
    welcome = input(prompt)
    
    if welcome == "Car": #if user enters "Car", new instance of car will be created and the details of the selections will print
        new_Car = Car() 
        print(f'''Here are the details of your new car:\n Make: {new_Car.get_Model()}\n Model:{new_Car.get_Model()}\n Color: {new_Car.get_Color()}\n Fuel Type: {new_Car.get_Fuel_Type()}\n Engine Size: {new_Car.get_Engine_Size()}\n Number of Doors: {new_Car.get_Num_Doors()}\n Options:{new_Car.get_options()}''')
        # functions created in parent and Car child class are called
        print()

    elif welcome == "Pickup": #if user enters "Pickup", new instance of car will be created and the details of the selections will print
        new_Pickup = Pickup()
        print(f''' Here are the details of your new Pickup:\n Make: {new_Pickup.get_Model()}\n Model:{new_Pickup.get_Model()}\n Color: {new_Pickup.get_Color()}\n Fuel Type: {new_Pickup.get_Fuel_Type()}\n Cab Style: {new_Pickup.get_Cab_Style()}\n Bed Length: {new_Pickup.get_Bed_Length()}\n Options: {new_Pickup.get_options()}''')
        #functions created in parent and Pickup child class are called
        print()
    elif welcome == "done": # if user enters done, then program will end
        break

    

    
