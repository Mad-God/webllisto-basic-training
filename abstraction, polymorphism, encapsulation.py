# ***************** ABSTRACTION ********************

# hiding unnecessary details to reduce complexity


# abstract classes and methods
    # extend from ABC as meta_class
    # can have abstract and concrete methods
    # PVM(python virtual machine) can not create instances of this class





"""
from abc import ABCMeta, abstractmethod, ABC

class Shape(ABC):

    def __init__ (self, shapeType):
        pass
       

    @abstractmethod 
    def area(self) :
        print("vbbgfsdf")
        pass


    @abstractmethod
    def perimeter (self):
        print("perimeter is:")
        pass

    def get_class_name(self):
        return self.__class__




class Shape2:

    # __metaclass__ = ABCMeta (in case you're not extending ABC)
       

    @abstractmethod 
    def area(self) :
        print("area: ", end = "")
        pass


    @abstractmethod
    def perimeter (self):
        print("perimeter is: ")
        pass

    def get_class_name(self):
        return self.__class__







class Rectangle(Shape):

    def __init__(self, length, breadth):

        self.length = length 

        self.breadth = breadth

    def area (self):

        return self.length * self.breadth

    def perimeter (self):

        return 2 * (self.length + self.breadth)



class Rectangle2(Shape2):

    def __init__(self, length, breadth):

        self.length = length 

        self.breadth = breadth

    # def area (self):
    #     return self.length * self.breadth

    # def perimeter (self):
    #     return 2 * (self.length + self.breadth)




class Circle (Shape):
    pi = 3.14
    def __init__ (self, radius):


        self.radius = radius

    def area (self):
        # super.area()              # type object 'super' has no attribute 'area'
        print(super)
        return round(Circle.pi * (self.radius ** 2), 2)

    def perimeter(self):

        return round (2 * Circle.pi * self.radius, 2)

c = Circle(3)


# print(c.perimeter())
print(c.get_class_name())


c2 = Circle(3)


print(c2.area())
print(c2.get_class_name())          # using the concrete method


# s = Shape()                       # throws error

s = Rectangle2(2,3)
print(s.get_class_name())
print(s.perimeter())


r = Rectangle2(3, 4)

print(r.area())
print(r.perimeter())"""


# ***************** ENCAPSULATION *******************
# wrap data into units
# uses plain attributes to achieve encapsulation


# _varname for protected vars
# __varname for private vars


# class Edureka():
#     def __init__(self):
#         self.c = "edu"
#         self.__t = "pyt"
#     def cname(self):
#         return self.c +" : "+ self.__t

# ob = Edureka()

# print(ob.c)
# # print(ob.__t)                 # cant acces this variable cause private
# print(ob._Edureka__t)           # name mangling
# print(ob.cname())

# we can use getter and setter function to give acces to private attributes





# ***************** POLYMORPHISM *******************

# duck typing
# operator overloading
# method overloading
# method overriding

# DUCK TYPING
"""
    class Pycharm:

        def execute(self):
            print("Compiling")
            print("Running")

    class MyEditor:
        def execute(self):
            print("Spell Check")
            print("Convention Check")
            print("Compiling")
            print("Running")

    class Laptop:

        def code(self,ide):
            ide.execute()

    ide = MyEditor()
    ide = PyCharm()         #doesn't matter class's of object it is as long as it has .execute()

    lap1 = Laptop()
    lap1.code(ide)

"""


# OPERATOR OVERLOADING
"""
    
    +	__add__(self, other)
    -	__sub__(self, other)
    *	__mul__(self, other)
    /	__truediv__(self, other)
    //	__floordiv__(self, other)
    %	__mod__(self, other)
    **	__pow__(self, other)
    &	__and__(self, other)
    |	__or__(self, other)



    <	__lt__(self, other)
    >	__gt__(self, other)
    <=	__le__(self, other)
    >=	__ge__(self, other)
    ==	__eq__(self, other)
    !=	__ne__(self, other)



    -	__neg__(self)
    +	__pos__(self)
    ~	__invert__(self)

"""





# METHOD OVERLOADING

# class cl:
#     def Hello(self, name=None):
#         if name is not None:
#             print('Hello ' + name)
#         else:
#             print('Hello ')
            
# # Create an instance
# obj = cl()
    
# # Call the method
# obj.Hello()
    
# # Call the method with a parameter
# obj.Hello('RAm')

