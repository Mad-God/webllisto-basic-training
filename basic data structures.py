# *********************** Numbers ****************************
"""
    # int: 5
    # float: 5.0
    # complex: 2+4j
    # exponential: 1e7


    # for bases other than 10:

    x = 0b1001    
    y = 0o2312
    z = 0x1ac231d

    # print(x,y,z)           # 9 1226 28058397



"""


# ************************* Strings **************************
"""
    # multiline string
    a = '''sadasd
    asdasdasd
    asdasdasd
    asdasdasd'''


    # print("asd" in a)   # check for substring in string


    start = 2
    end = 17
    step = 3

    # print(a[start:end:step])         # print only specified range of string with mentioned steps after each character

    del a                 # delete the string object



    # formatting the string
    a = "{:.2f} is the first, {} is the second argument.".format(123, 456)
    print(a)

    # or we can give indices or keywords to the {} so that the order of parameters is not fixed.






    ''' String methods

        a.upper()

        a.lower()

        a.strip()

        a.replace("a", "x")

        a.split()
        a.center(30, "*")


        capitalize(), casefold() lower case, center(width, fillchar), count(value),
        a.encode(encoding), a.expandtabs(tabsize), a.find(sub), a.format(), a.index(sub),
        a.isdigit(), isalnum, isalpha, isascii, isdecimal, islower, isnumeric, isspace, istitle, isupper, 
        a.join(iterable), lower(), a.partition(sep) returns a string parted into 3 parts, replace(), 
        a.split(), splitlines(), startswith(), swapcase(), title(), 

    '''

    # print raw string by using 'r' prefix before strings
    print(r"string are used to print strings as they are without the escape characters like \n")

    # print f-strings for easier formatting of strings
    print(f"{start} is the start, end is {end} ")



"""



# ************************* List *****************************


"""
    lst = list(("asdasd", "ads", 321, 543, "asda", 3, "d2edesd"))

    print(lst)


    print(lst[0::2])




    # list methods
    
        lst.append()
        lst.clear()
        lst.copy()    # copy of the list
        lst.count()
        lst.extend()
        lst.index()         # first occurence
        lst.insert(index, object)  
        lst.pop(index)

        lst.remove(object)

        lst.reverse()

        lst.sort()
        del lst

    [1,2,3,4] pop(2)
    100 == 100
    100 is 100
    1000 is 1000
    1000 == 1000



"""



# ************************ Dictionary ***********************

"""

    # allowed dataypes for keys: bool, int, float, string
    # values can be of any datatype


    # dicts are ordered (since python 3.7), changeable

    d = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
    }

    print(d)

    d.clear()
    x = d.copy()        # make a copy of the dictionary, instead of just assigning the same referance value to x variable
    d.get(key, default_return_value_if_doesn't_exist)



    d.fromkeys(keys_list, value)        # set the value of keys_list items keys in the dict as the "value" parameter

    d.items(), keys(), values(),
    d.pop(key)
    d.popitem()     # random item removed(in py 3.7); before that the last added item removed

    d.setdefault(key, optional_default_value)       # get the value of key or set it to optional_default_value


    d.update(another_dict)



"""





# *********************** Tuple *****************************
"""
    # ordered and unchangeable. Can have duplicates. Items of any datatype. no adding or removing from  a tuple.

    tup = ("apple",)        # tuple with only one item
    tup2 = ("apple")         # considered as a string

    t = tuple(())
    print(t)
    print(type(t))          # ('a', 's', 'd', 'a', 'd')
    
    t += tup            # you can add two tuples
    t2 = t*2

    (x,y,*z) = t           # unpacking a tuple, like in javascript


    # tuple methods
    count(object)       
    index(object)
    


"""




# ************************* Sets *****************************
"""
    mset = {1,2,3,4,5,6}


    # unordered, sets are changeable but set items are unchangeable, unindexed.
    # Duplicate values are ignored

    mset2 = set(("sadasd", "SAdsad", "ad",213,213,12323,321,321))       # using the set constructor

    # to access the items of a set, you must use a loop or use the in operator


    # to add items in set
    mset.add("saddsa")

    mset.update({7,8,9,0})        


    mset.update({"asd":231, "adsd":4635})     # only adds the keys of the dict


    # set methods 

    .add()
    .clear()
    .copy()
    .difference(set2)
    .difference_update(set2)
    .discard(object)        # throws an error if element not present
    .intersection(set2)
    .isdisjoint()
    .issubset()
    .issuperset()
    .pop()          # any element
    .remove()       # specified element
    .symmetric_difference()
    .union()
    .update()



"""







# immutablility of tuple, is and == difference, discard and remove, integer objects less than ceratin limit always present in memory








