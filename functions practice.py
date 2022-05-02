# """ 
# docstrings
# why funcs
# what funcs
# types of funcs

# """




# Why?
    # DRY approach
    # for menu based/ repetetive functionality





# def stands for define
# docstring stands for documentation string



# types of funs:
    # based on definition
        # built-in
        # user defined
    
    # based on return and parameter
        # no param no return(None)
        # no para but return val
        # param but no return val(None)
        # param and return val both





# functions vs methods:
    # metthods are associated w a class, functions are standalone
    # methods are accessed using class's object, functions access directly using their name or alias
    # all methods are functions but all functions are not methods





# parameters vs arguments:
    # parameters are names used in func definition, arguments are the values passed to the function





# types of arguments:
    # default
    # required
    # keyword
    # variable number of arguments, keyword arguments





# built-in funcs:
    # abs() it return the absolute value. In case of complex numbers, it first converts the value to its magnitude, then returns the magnitude
    # all() return true if all items are true in the iterable. If iterable empty, still true
    # some() return true if all items are true in the iterable. If iterable empty, still true
    # ascii() return an ascii readable string of any object passed as parameter. Non-ascii characters are replaced with escape sequence
    # enumerate(iterable, start) return enumerate object of iterable for index of each element with its index
    # getattr(object, attr_name, default:optional) get the value of the attribute from the given object, or default 
    # setattr(object, attr_name, value)
    # min(iterable)
    # pow(base, exponent, modulo:optional)
    
    # map(func_name, iterable)
    # filter()
    # reduce()






# lambda functions/ anonymous functions:



    # x1 = lambda x,y:x+y

    # print(x1(2,3))



    # l = map(lambda x:x*3, [1,2,3,4,5])
    # print(list(l))

    # from functools import reduce
    # l = reduce(lambda x,y:x*y, [1,2,4,6,7,8])
    # print((l))


    # l = filter(lambda x:x<10, [1,2,12,32,54,4,3])
    # print(l)

    # print(list(l))
    # for i in l:
    #     print(i)





# returning multiple values, adding a docstring
    # def x():
    #     """
    #     retunr a tuple sadasdasdasd
    #     """
    #     return (2,3,4)

    # *n,y = x()
    # help(x)
    # # print(help(x))




# gloabl vs local scope:

    # num = 5
    # num2 = 6
    # num3 = 4
    # def x():
    #     num2 = 7
    #     global num3
    #     num3 = 3
    #     num4 = 20
    #     print(num, num2, num3, num4)
        
    #     def y():
    #         global num4
    #         num4 = 30
    #         print(num4)
    #         num3 = 2
    #         print(num, num2, num3)
            
    #     y()
    #     print(num, num2, num3, num4)

    # print(num, num2, num3)

    # x()
    # # y()       # throws error

    # print(num, num2, num3)





# recursive functions:
    # def pallindrome(s):
    #     print(s)
    #     if len(s) <= 1:
    #         print("cond1")
    #         return True
    #     elif len(s) == 2:
    #         print("cond2")
    #         if s[0] == s[1]:
    #             print("cond2.1")
    #             return True
    #         else:
    #             return False
    #     elif s[0] == s[-1]:
    #         print("cond3")
    #         return pallindrome(s[1:-1])
    #     else:
    #         return False


    # print(pallindrome("sqsaasqss"))


