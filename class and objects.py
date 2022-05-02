# inheritance

# class Fruit:
#     def __init__(self, tex, sweet) -> None:
#         self.texture = tex
#         self.sweet = sweet




# class Veggy:
#     def __init__(self, tex, salty) -> None:
#         self.texture = tex
#         self.salty= salty






# class Apple(Fruit):
#     color = ""
#     weight = 10
#     loc = "ind"
#     def __init__(self, color, w, c):
#         self.color = color
#         self.weigth = w
#         self.price = c

#     def __bool__(self):
#         return bool(0)

#     def cost(self, amt):
#         return self.price * amt



# class Tomato(Fruit, Veggy):
#     color = ""
#     weigth = 0

#     def __init__(self, color, w, c):
#         self.color = color
#         self.weigth = w
#         self.price = c

#     def __bool__(self):
#         return bool(0)

#     def cost(self, amt):
#         return self.price * amt




# x = Apple("Orange", 50, 20)
# print(x.weigth, x.color)
# x.weigth = 0
# print(x.weigth, x.color)
# print(bool(x))
# print(Apple.weight)
# print(x.loc)
# x.loc = "rus"
# # print(dir(x))

# Apple.loc = "russ"
# print(x.loc)
# y = Apple("Red", 30, 30)
# print(y.loc)
# print(Apple.loc)
# # print(dir(x))
# print(x.loc)



# multiple inheritance

# class Class1:
#     def m(self):
#         print("In Class1")
 
# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()
 
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()
 
# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")  
#         # Class3.m(self)
#         super().m()
    


# obj = Class4()
# obj.m()

# print(Class4.mro())         #This will print list
# print(Class4.__mro__)        #This will print tuple






# static variables

# class Employee: # create Employee class name  
#     dept = 'Information technology'  # define class variable  
#     def __init__(self, name, id):  
#         self.name = name       # instance variable  
#         self.id = id             # instance variable  
  
# # Define the objects of Employee class  
# emp1 = Employee('John', 'E101')          
# emp2 = Employee('Marcus', 'E105')  
  
# print (emp1.dept)   
# print (emp2.dept)   
# print (emp1.name)   
# print (emp2.name)   
# print (emp1.id)    
# print (emp2.id)   
  
# # Access class variable using the class name  
# print (Employee.dept) # print the department  
  
# # change the department of particular instance  
# emp1.dept = 'Networking'  
# print (emp1.dept)   
# print (emp2.dept)   
  
# # change the department for all instances of the class  
# Employee.dept = 'Database Administration'  
# print (emp1.dept)   
# print (emp2.dept)  




# static, instance, class methods, 

class Student:

    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info(self, x = 23):
        print(self)
        print("This is Student class.. in abc molude", self, x)

    # def info(x,y):


    # def get_m1(self):
    #     return self.m1
    #
    # def set_m1(self,value):
    #     self.m1 = value

s1 = Student(34,47,32)
s2 = Student(89,32,12)



print(s1.avg())
print(Student.getSchool())

Student.info(25)



# magic methods

"""
    __init__

    The _init_ method is called after the instance of the class has been created but
    before it returned to the caller. It is invoked without any call, when an instance of the
    class is created like constructors in other programming languages such as C++, Java, C#, PHP, etc.
    These methods are also known as initialize and are called after _new_. Its where you should 
        initialize the instance variables.

    __str__

    This function computes "informal" or a nicely printable string representation of an object and
    must return a string object.

    __repr__

    This function is called by the repr() built-in function to compute the "official"
    string representation of an object and returns a machine-readable representation of a type. 
    The goal of the _repr_ is to be unambiguous.

    __len__

    This function should return the length of an object.

    __call__

    We can make an object callable by adding the _call_ magic method

    If defined in a class, then that class can be called. But if it was a function, 
    instance itself rather than modifying.

    __del__

    Just as _init_, which is a constructor method, _del_ is like a destructor. 

    __ge__

    This method gets invoked when >= operator is used and returns True or False.

    __neg__

    This function gets called for the unary operator.

    __ipow__

    This function gets called on the exponents with arguments. e.g. a**=b.

    __le__

    This function gets called on comparison using <= operator.

    _nonzero_

    This function returns the Boolean value of the object. 
    It gets invoked when the bool(self) function is called.

"""


