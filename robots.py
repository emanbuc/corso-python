class Robots:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]  # Starting at origin
        print(f"Robot {self.name} initialized at position {self.position}.")
    
    def eat(self):
        print("I'm hungry")

    def walk(self,x):
        if isinstance(x, int):
            self.position[0] += x
            print(f"Robot {self.name} walked to position {self.position}.")
        else:
            raise ValueError("Distance must be an integer.")

class Robot_Dog(Robots):
    
    def make_noise(self):
        print(f"{self.name} says: Woof!")
    
    def eat(self):
        print(f"{self.name} is eating dog food.")
        
my_robot = Robot_Dog("Rex")
my_robot.walk(5)
my_robot.make_noise()
my_robot.eat()
    