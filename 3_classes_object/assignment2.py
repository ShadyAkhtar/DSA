# 1. Define a python class Person with instance object variables name and age. Set
# Instance object variables in _init_() method. Also define show() method to display
# name and age of a person.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'Name: {self.name}, Age: {self.age}')

p1 = Person("shadab", 25)
p1.show()

# 2.
# Define a class Circle with instance object variable radius. Provide setter and getter
# for radius. Also define getArea and getCircumference() methods.
import math

class Circle():
    def __init__(self, radius=0):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(2)
print("RADIUS", circle.get_radius())
print("AREA", circle.get_area())
print("CIRCUMFERENCE", circle.get_circumference())

circle.set_radius(3)
print("RADIUS", circle.get_radius())
print("AREA", circle.get_area())
print("CIRCUMFERENCE", circle.get_circumference())

# 3.
# Define a class Rectangle with length and breadth as instance object variables.
# Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle():
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    def set_dimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def show_dimension(self):
        print(f'Length: {self.length}, Breadth: {self.breadth}')
        
    def get_area(self):
        return self.length * self.breadth
    
rect = Rectangle(2, 2)
rect.show_dimension()
print(rect.get_area())
rect.set_dimensions(4, 3)
rect.show_dimension()
print(rect.get_area())



# 4.
# Define a class Book with instance object variables bookid, title and price. Initialise
# them via _init_() method. Also define method to show book variables.


class Book:
    def __init__(self, bookid, title, price):
        # Initialize instance variables
        self.bookid = bookid
        self.title = title
        self.price = price

    def show_info(self):
        # Display book information
        print(f"Book ID: {self.bookid}")
        print(f"Title: {self.title}")
        print(f"Price: ${self.price:.2f}")

# Example usage:
# Creating an instance of the Book class
book1 = Book(bookid=1, title="Python Programming", price=29.99)

# Calling the show_info method to display book information
book1.show_info()


# 5.
# Define a class Team with instance object variable a list of team member names.
# Provide methods to input member names and display member names.
# 125% ^


class Team():
    def __init__(self):
        self.members = []

    def set_member_name(self):
        num_of_member = int(input("please enter number of team member: "))
        for _ in range(num_of_member):
            member_name = input("enter team member name: ")
            self.members.append(member_name)
    
    def display_member_names(self):
        return self.members

team = Team()
team.set_member_name()
print(team.display_member_names())