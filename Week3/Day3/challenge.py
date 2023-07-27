from math import pi
import turtle

#Daily Challenge : Circle

class Circle:
    def __init__(self, length, measurement = "radius") -> None:
        if (measurement == 'radius'):
            self.radius = length
            self.area = pi * length * length
        else:
            self.radius = length / 2
            self.area = pi * length * length / 4
    def __add__(self, other):
        if type(other) == Circle:
            return Circle(self.radius+other.radius)
    def __gt__(self, other):
        if (self.radius > other.radius):
            return(True)
        else:
            return(False)
    def __lt__(self, other):
        if (self.radius < other.radius):
            return(True)
        else:
            return(False)
    def __repr__(self):
        return(f"Circle({self.radius}, {self.area})")
    def __eq__(self, other):
        if (self.radius == other.radius):
            return True
        else:
            return False
    def __str__(self):
        return(f"This is a circle with Radius = {self.radius}, area = {self.area}")
        
value_type = input("Please choose what value you will provide: Radius or Diameter (type 'r' or 'd') to choose ")
if (value_type != 'd'):
    value_type = 'radius'
else:
    value_type = 'diameter'
value = int(input(f"write circle {value_type} "))
circle_one = Circle(value, value_type)
circle_two = Circle(value+20, value_type)
circle_three = Circle(value+1, value_type)
circle_four = Circle(value+1, value_type)

print(circle_one)
print(circle_one > circle_two)
print(circle_one == circle_three)
print(circle_two == circle_three)

circle_list = [circle_two, circle_four, circle_one, circle_three]
print(circle_list)
circle_list.sort()
print(circle_list)



s = turtle.getscreen()
t = turtle.Turtle()

for x in circle_list:
    t.circle(x.radius)
    t.forward(x.radius*2)