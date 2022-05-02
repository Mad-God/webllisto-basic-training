# *************** Iterator *******************



# an iterator is an object with a state that remembers where it was during an iteration
    # it has a next value using dunder next method in an iterator.
    # List, dont have this __next__ method, so they aren't iterators
    # we can access the next value using:
    # next(itr) or the iter.__next__

    # we can use iter(iter) or the iter.__iter__ method on any iterator(list, set, etc) that returns an iterator of that object

    # iterators have to have an __iter__ method despite being iterators themselves, because it tells python that it an iterable. It just return self


# iterators properties:
    # only go forward
    # no resetting it


# remaking the range function


class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1,10)
# for num in nums:
#     print(num)


# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))



 

# generator based implementation of the MyRange class

def myrange(start, end):
    current = start
    while current < end:
        yield current
        current += 1
        
nums = myrange(1,5)
# print(next(nums))
# print(next(nums))
# print(next(nums))

# for i in nums:
#     print("asdads", i)
# print(next(nums))





# making iterators going forever
    # there is no template code for this, just remove the conditions and the end value, keep on yielding and incrementing the current value


# example:
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentence('This is a test')

# for word in my_sentence:
#     print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))






# ********************************************

# *************** Generator ******************



# functions that act as iterators, and produce elements 'on demand'



def g():
    yield 1
    yield 2
    yield 3
    yield 4


x = g()

# print(next(x))






# generator expressions:
# import itertools
# import sys

# squares = (x**2 for x in itertools.count(1))
# sqs = (x**2 for x in range(30))

# for x in sqs:
#     # print(x)

#     if x > 500:
#         sqs.close()

# # print(type(sqs))




# using iterators with files

# if using files through pandas, we can specify chunk_size parameter in the read_csv() method

# f = open("day.txt")

# def file_iterator():
#     while True:
#         x =  f.readline()
#         if x == "":
#             break
#         yield x

# x = file_iterator()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# reader = file_iterator()

# while True:
#     try:
#         print(next(reader))
#     except:
#         print("EOF")
#         break






# ********************************************



# *************** Decorator ******************


# closures: they are records storing a function together with an environment and the variables

# def outer(msg):
#     def inner():
#         print(msg)
#     return inner

# x = outer("x")
# z = outer("z")

# x()
# z()

# x()
# z()




# Decorators:
    # a function that takes another function as argument amnd returns a new function



def dec(org_func):
    def wrap():
        print("before wrapping function ran the function " + org_func.__name__)
        org_func()
    return wrap



# def disp():
#     print("ran disp")

# @dec
# def readnot():
#     print("ran readnot")



# deco = dec(disp)
# deco()


# readnot()


# pasing values to the decorators and wrapped functions

# def dec2(org_func):
#     def wrap(*args, **kwargs):
#         print(kwargs["for_deco"])
#         kwargs.pop("for_deco")
#         print("before wrapping function ran the function " + org_func.__name__)
#         org_func(*args, **kwargs)
#     return wrap


# @dec2
# def readnot2(id):
#     print("ran readnot: " + str(id))

# readnot2(12, for_deco = 23)





def login_required_deco(show_data):
    def wrapper(*args, **kwargs):
        x = kwargs.pop("password")
        if x:
            show_data(*args, **kwargs)
        else:
            print("Passwrod Required")
    return  wrapper



# @login_required_deco
# def show_data(id, marks):
#     print("id: ", id, "marks", marks)




# show_data(id = 23, marks = 87, password = "")

# show_data(id = 23, marks = 87, password = "abracadabra")




# classes as decorators

class Deco(object):
    pass
    def __init__(self, org):
        self.org = org
        self.__name__ = 'Deco'

    def __call__(self, *args, **kwargs):
        x = kwargs.pop("password")
        if x:
            self.org(*args, **kwargs)
        else:
            print("Passwrod Required")

    # def __name__(self):
    #     return 'Deco'


# def dec(org_func):
#     def wrap(*args, **kwargs):
#         print("before wrapping function ran the function " + org_func.__name__)
#         org_func(*args, **kwargs)
#     return wrap


# print(dir(Deco))


@dec
@Deco
def show_data2(id, marks, *args, **kwargs):
    print("id: ", id, "marks", marks)
x = input()
show_data2(id = 23, marks = 45, password = x)







# login deco exercise

def login_required_deco1(show_data):
    def wrapper(*args, **kwargs):
        x = kwargs.get("password")
        y = kwargs.get("uname")
        if x == "satayam@#$" and y == "satyam@webllisto.com":
            show_data(*args, **kwargs)
        else:
            print("Invalid Credentials")
    return wrapper



@login_required_deco1
def show_data1(id, marks, **kwargs):
    print("id: ", id, "marks", marks)

y = input("enter username: ")
x = input("enter passwrod: ")

show_data1(id = 23, marks = 87, password = x, uname = y)






# ******************************************** 