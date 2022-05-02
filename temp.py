class Edureka2():
    def __init__(self):
        self.c = "edu"
        self.__t = "pyt"
        self._s = "subject"
    def cname(self):
        return self.c +" : "+ self.__t

# ob = Edureka2()

# print(ob.c)
# # print(ob.__t)                 # cant acces this variable cause private
# print(ob._Edureka__t)           # name mangling
# print(ob.cname())