from datetime import datetime, time
import sys


class User:
    def __init__(self, name, pwd, username, email, phone, address):
        self.name = name
        self.pwd = pwd
        self.username = username
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        str = f"name: {self.name}, email: {self.email}, address: {self.address}, "
        return str





class Member(User):
    id = 0
    def __init__(self, name, pwd, username, email, phone, address, lib):

        self.id = Member.id
        Member.id += 1
        self.user = User(name, pwd, username, email, phone, address)
        self.issues = {}
        self.balance = 0
        self.library = lib
        self.history = []


    def __str__(self):
        return str(self.id)+ "- " + str(self.user)


    def member_functions(self):
        while True:        
            print("\n\n1. Issue Books")
            print("2. Show Issued Books")
            print("3. Check Previous Issues")
            print("4. Return Book")
            print("5. Pay Dues")
            print("6. Check Fine")
            print("7. Show all books in library")
            print("8. Exit")
            x = int(input("Enter your choice:"))
            if x == 1:
                self.issue_book()
            elif x == 2:
                self.show_issued_books()
            elif x == 3:
                self.previous_issues()
            elif x == 4:
                self.return_book()
            elif x == 5:
                self.payment()
            elif x == 6:
                self.check_fine()
            elif x == 7:
                self.show_allBooks()
            else:
                return


    def issue_book(self):
        name = input("\nEnter book name: ")
        for i in self.issues:
            if name in i.name:
                print("Book already issued !!")
                return 
        book = None
        x = -1
        for i in  range(len(catalogs)):
            book = catalogs[i]
            print(book)
            if book.name == name:
                x = i
                print("book found at index", i)
                break
        if x == -1:
            print("Book could not be found !!")
        elif book.stock < 1:
            print("Book out of stock !!")
        else:
            print("Currently in stock: ", book.stock)
            stock = int(input("How many copies do you want?"))
            if stock > book.stock:
                print("We don't have that many copies !!")
                return 
            print("book issed", book)
            now = datetime.now()
            # c_time = now.strftime("%H:%M:%S")
            book.stock -= stock
            self.issues[book] = (now, stock)
            lib = self.library
            lib.issues.append((self, book, stock, now, False))
            lib.issue_num += 1
            self.balance += 10 * stock
    
    
    def show_issued_books(self):
        print("\nThis is all your issues: ")

        for book in self.issues:
            print(book, " issued on: ", self.issues[book][0], ", copies: ", self.issues[book][1])
            

    
    def previous_issues(self):
        print("\nThis is all your previous history till now issues: ")

        for book, t, f, s in self.history:
            if f:
                print(book, f" issued {s} copies on: ", t, ". Fine was charged")
            else:
                print(book, f" issued {s} copies on: ", t)



    def return_book(self):
        name = input("\nEnter book name: ")
        book = False
        for issue in self.issues:
            if name == issue.name:
                book = issue


        if not book:
            print("Book not found in your issue list!! \n\n")
            return

        copies  = self.issues[book][1]
        r_time = self.issues[book][0]
        if r_time.second + 5 < 59:
            r_time = time(r_time.hour, r_time.minute, r_time.second + 5)
        else:
            r_time = time(r_time.hour, r_time.minute + 1, (r_time.second + 5) % 6)
        print("Return time was: ", r_time)
        now = datetime.now()
        now = time(now.hour, now.minute, now.second)
        c_time = now.strftime("%H:%M:%S")
        fined = False
        if now > r_time:
            print("You are late on returning the book. You are fined $5. ")
            self.balance += 5
            fined = True

        lib = self.library

        for i, b in lib.book_dict.items():
            if b == book:
                # print(book, " had copies: ", book.stock)            
                book.stock += copies
                # print(book, " now has copies: ", book.stock)            

        # update the book to library history
        for ind in range(len(lib.issues)):
            i = lib.issues[ind]
            # print(i)
            if i[0] == self:
                # print("self matched")
                if i[1] == book:
                    # print("catalog matched")
                    if i[3] == self.issues[book][0]:
                        # print("time matched")
                        # print(i)
                        # print(id(i))
                        i = list(i)
                        # print(i[-1])
                        i[-1] = True
                        i = tuple(i)
                        lib.issues[ind] = i
            # else:
            #     print(i, "\nwas mathed with\n",self, book, "stock", now, False)
                # pass

            # (self, book, stock, now, False) 
        self.history.append((book, now, fined, copies))
        self.issues.pop(book)

    
    def show_allBooks(self):
        self.library.showAllBooks()



    def payment(self):
        print("\nYour current outlying balance is: ", self.balance)
        pay = int(input("How much would you linke to pay now?: "))
        self.balance -= pay
        print("\nYour updated balance is: ", self.balance)



    def check_fine(self):
        print("\nYour current outlying balance is: ", self.balance)
        print("\nThis is all your current issues: ")
        print(self.issues)
        for book, [t,c] in self.issues.items():
            print(book, " issued on: ", t, "coies: ", c)


        # print("\nThis is all your previous issues: ")
        # # print*self.his
        # for book, t, f, c in self.history:
            # if f:
                # print(book, " ", c, "copies issued on: ", t, ". Fine was charged")




class Librarian(User):
    id = 0

    def __init__(self, name, pwd, username, email, phone, address, lib):
        self.id = Librarian.id
        Librarian.id += 1
        self.library = lib
        self.user = User(name, pwd, username, email, phone, address)

    
    def __str__(self):
        return str(self.id)+ "- " + str(self.user)


    def librarian_functions(self):
        while True:
            
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Show all books")
            print("4. exit")
            x = int(input("Enter your choice:"))
            if x == 1:
                self.add_book()
            elif x == 2:
                self.remove_book()
            elif x == 3:
                self.show_allBooks()
            else:
                return

    def add_book(self):
        name = input("Enter the book name: ")
        for i in catalogs:
            if i.name == name:
                print("Book with same name alreaday exists.")
                return
        author = input("Enter the author name: ")
        stock = int(input("Enter the number of copies: "))
        x = Catalog(name, author, self.library, stock)
        catalogs.append(x)



    def remove_book(self):
        name = input("Enter book name: ")
        x = -1
        for i in  range(len(catalogs)):
            book = catalogs[i]
            if book.name == name:
                x = i
            
        if x == -1:
            print("Book could now be found !!")
        else:
            print(catalogs[x] , "has been removed. ")
            self.show_allBooks()

            
            def del_from_dict(self):
                lib = self.library
                for i, j in lib.book_dict.items():
                    # print(j, self)
                    if j == self:
                        lib.book_dict.pop(i)
                        print("deleted the book: ", self)
                        return 
                print("book not deleted.")
                # print("Books_dict for ", lib.name, ": ", lib.book_dict)

            del_from_dict(catalogs[x])


            # self.library.book_dict.pop(x)
            # print("ref count for given catalog: ",sys.getrefcount(catalogs[x]))
            # cat = catalogs[x]
            # cat.remove_from_dict()
            # cat.__del__()
            # print(type(cat))
            catalogs.pop(x)
            # print("new catalogs: ", catalogs)

    
    def show_allBooks(self):
        self.library.showAllBooks()




class Library:
    def __init__(self, name, book_dict = {}):
        self.name = name 
        self.book_dict = book_dict
        self.books_num = 0
        self.issue_num = 0
        # self.history = 0
        self.issues = []
        # self.history = []

    def showAllBooks(self):
        print("\nHere are all the books we have: ")
        for i,j in self.book_dict.items():
            print(i, end = ": ")
            print(self.book_dict[i])
        # print("\n\nThe catalogs list: ", catalogs)
        input()

    def showAllIssues(self):
        pass



class Catalog:

    def __init__(self, name, author, lib, stock):
        self.name = name
        self.author = author
        self.library = lib
        self.stock = stock
        lib.book_dict[lib.books_num + 1] = self
        lib.books_num += 1
        


    def __str__(self):
        return self.name +" by "+ self.author + " currently stock: " + str(self.stock)


    def remove_from_dict(self):
        lib = self.library
        for i, j in lib.book_dict.items():
            if j == self.name:
                del lib.book_dict[i]
                print("deleted the book: ", self)
                return 
        print("book not deleted.")
        # print("Books_dict for ", lib.name, ": ", lib.book_dict)





# ************* DATA *******************

members = []
librarians = []
catalogs = []
libraries = []



def add_dummy_Data():
    lib1 = Library("Lib1", {})
    libraries.append(lib1)


    x = Member("mem1", "pwd1", "Member1", "mem@mem1", "memPhone1", "memHouse1", lib1)
    members.append(x)


    x = Member("mem2", "pwd2", "Member2", "mem@mem2", "memPhone2", "memHouse2", lib1)
    members.append(x)

    x = Member("mem3", "pwd3", "Member3", "mem@mem3", "memPhone3", "memHouse3", lib1)
    members.append(x)


    x = Member("mem4", "pwd4", "Member4", "mem@mem4", "memPhone4", "memHouse4", lib1)
    members.append(x)







    x = Librarian("lib1", "pwd1", "Librarian1", "lib@lib1", "libPhone1", "libHouse1", lib1)
    librarians.append(x)


    x = Librarian("lib2", "pwd2", "Librarian2", "lib@lib2", "libPhone2", "libHouse2", lib1)
    librarians.append(x)

    x = Librarian("lib3", "pwd3", "Librarian3", "lib@lib3", "libPhone3", "libHouse3", lib1)
    librarians.append(x)


    x = Librarian("lib4", "pwd4", "Librarian4", "lib@lib4", "libPhone4", "libHouse4", lib1)
    librarians.append(x)



    x = Catalog("cat1", "auth1", lib1, 5)
    catalogs.append(x)


    x = Catalog("cat2", "auth2", lib1, 5)
    catalogs.append(x)

    x = Catalog("cat3", "auth3", lib1, 5)
    catalogs.append(x)


    x = Catalog("cat4", "auth4", lib1, 5)
    catalogs.append(x)

add_dummy_Data()



# ************* Menu Pages **************



def front_page():
    print("\n\n\n\n")
    print("1. Sign-Up as Member")
    print("2. Sign-Up as Librarian")
    print("3. Member Log-In")
    print("4. Librarian Log-In")
    print("5. See all Data")
    print("6. Exit")
    return int(input("Enter your choice: "))

# https://github.com/Mad-God/webllisto-training-basic


def member_login_page():
    name = input("enter username: ")
    for i in members:
        if i.user.name == name:
            pwd = input("Enter password: ")
            if pwd == i.user.pwd:
                return i.member_functions()
            else:
                print("Wrong Password")
                return
    print("no member with given name found")





def librarian_login_page():
    name = input("enter username")
    for i in librarians:
        if i.user.name == name:
            pwd = input("Enter password: ")
            if pwd == i.user.pwd:
                return i.librarian_functions()
            else:
                print("Wrong Password")
                return
    print("no librarian with given name found")





def member_signup_page():
    print("\n\nOwner Signup page")
    accepted = False
    while not accepted:
        name = input("Enter your desired username: ")
        accepted = True
        for i in members:
            if name == i.user.name:
                print("Username already taken")
                accepted = False
    pwd = input("Enter your password :")
    username = input("Enter your Full name :")
    email = input("Enter your email :")
    mobile = input("Enter your mobile number :")
    address = input("Enter your adress :")

    x = Member(name, pwd, username, email, mobile, address, libraries[0])
    members.append(x)






def librarian_signup_page():
    print("\nCustomer Signup page")
    accepted = False
    while not accepted:
        name = input("Enter your desired username")
        accepted = True
        for i in librarians:
            if name == i.user.name:
                print("Username already taken")
                accepted = False
    
    pwd = input("Enter your password :")
    username = input("Enter your Full name :")
    email = input("Enter your email :")
    mobile = input("Enter your mobile number :")
    address = input("Enter your adress :")

    x = Librarian(name, pwd, username, email, mobile, address, libraries[0] )
    librarians.append(x)







def list_page():
    print("\nMembers: ")
    for i in members:
        print(i)
    print("\nLibrarians: ")
    for i in librarians:
        print(i)
    print("\nCatalogs: ")
    for i in catalogs:
        print(i)
    

    print("\nLibrary Issues: ")
    issuesLib = libraries[0]
    for i in issuesLib.issues:
        if i[-1]:
            print("Resolved", end = ": ")
            for x in i:
                print(i, end = " - ")
        else:
            print("Unsolved", end = ": ")
            print("Resolved",)
            for x in i:
                print(i, end = " - ")

    input()







while True:
    x = front_page()
    if x == 1:
        member_signup_page()
    elif x == 2:
        librarian_signup_page()
    elif x == 3:
        member_login_page()
    elif x == 4:
        librarian_login_page()
    elif x == 5:
        list_page()
    else:
        break

