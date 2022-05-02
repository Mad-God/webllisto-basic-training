"""
Implement a Bike Rental System with following features.

Customers

1. See available bikes on the shop
2. Rent bikes on hourly basis $5 per hour.

3. Rent bikes on daily basis $20 per day.

4. Rent bikes on weekly basis $60 per week.
5. Group Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price

Rental shops

1. Issue a bill when customer decides to return the bike.
2. Display available inventory
3. Take requests on hourly, daily and weekly basis by cross verifying stock

"""


 
from datetime import time, datetime
from tracemalloc import start

class Rental:
    def __init__(self, b, name):
        self.stock = b
        self.name = name


    def issue(self, issuer = None, period = 1):
        pass


    def update_stock(self):
        upd = int(input("How many bikes you have?: "))
        self.stock += upd


    def front_page(self):
        while True:
            print("\n\n\nYou have currently: "+str(self.stock)+" bikes")
            print("1. Update Inventory")
            print("2. View your issues")
            print("3. Logout")
            x = int(input("Enter your choice:"))
            if x == 1:
                self.update_stock()
            if x == 2:
                self.view_issues()
            else:
                return


    def view_issues(self):
        for i in issues:
            if i.shop == self:
                print(i)
        input()


    def __str__(self):
        return self.name+" has currently: "+str(self.stock)+" bikes"



class Customer:

    def __init__(self, n):
        self.name = n
    

    def issue(self):
        c = 1
        print("The available shops are: ")
        for i in shops:
            print(str(c)+". " + str(i))
            c += 1
        shop_num = int(input("Enter the Shop you want to issue from: "))
        print(shops[shop_num-1])
        shop = shops[shop_num-1]
        accepted = True
        while accepted:
            b_num = int(input(("How many do you want?")))
            if b_num > shop.stock:
                print("Isue limit over available stock...currently available bikes: ", shop.stock)
                accepted = True
            else:
                accepted = False
        
        t_num = int(input(("For how long?")))

        t_unit = int(input("1. Hours\n2. Days\n3. Weeks"))
        t_units = dict(enumerate(["Hours", "Days", "Weeks"], start = 1))
        
        print(t_units)
        
        
        now = datetime.now()
        c_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        if now.minute + t_num < 60:
            r_time = time(now.hour, now.minute + t_num, now.second)
        else:
            r_time = time(now.hour + 1, (now.minute + t_num) % 60, now.second)
        r_time_str = r_time.strftime("%H:%M:%S")
        print(type(c_time))
        print((c_time))

        c_shop = shops[shop_num-1]
        print(f"You are issuing {b_num} bike(s) from {c_shop.name} for {t_num} {t_units[t_unit]} at time: {c_time}")
        print(f"The return time is: {r_time_str}")

        i = Issue(self, c_shop, t_num, t_unit, b_num)


    def pay(self, company):
        pass


    def front_page(self):
        while True:
            # print("\n\n\nYou have currently issued: "+str(self.stock)+" bikes")
            print("\n\n\n1. Issue Bike")
            print("2. Return Bike")
            print("3. View Issues")
            print("4.Logout")
            x = int(input("Enter your choice:"))
            if x == 1:
                self.issue()
            elif x == 2:
                self.return_bike()
            elif x == 3:
                self.view_issues()
            else:
                return

    
    def view_issues(self):
        for i in issues:
            if i.customer == self:
                print(i)
        input()


    def return_bike(self):
        c_issues = []
        for i in issues:
            if i.customer == self and not i.returned:
                c_issues.append(i)
        c = 0
        for i in c_issues:
            c += 1
            print(c, ". ", i)
        i_num = int(input("Choose which issue you want to close: "))
        issue = c_issues[i_num-1]
        issue.close()
        print(issue.t_unit)
        if issue.t_unit == 1:
            r = 5
        elif issue.t_unit == 2:
            r = 20
        elif issue.t_unit == 3:
            r = 60
        price = issue.period * r
        now = datetime.now()
        # now = now.strftime("%H:%M:%S")

        # if now.minute + self.period < 60:
        now = time(now.hour, now.minute, now.second)
        # else:
        #     now = time(now.hour + 1, (now.minute + self.period) % 60, now.second)
        


        print(now)
        print(type(issue.time))
        print(type(issue.return_time))
        print(type(now))
        print((issue.time))
        print((issue.return_time))
        print((now))
        
        print(issue.return_time)
        if now > issue.return_time:
            price += price * 0.3
            print("You are being penalized for late return. $", price)
        if issue.bikes > 5:
            price -= price * 0.2
            print("You get the discount for group purchase of bikes. $", price)
        print(f"You are liable to pay: ${price}")
        issue.price = price




class Issue:
    def __init__(self, c, s, p, tu, bu):
        self.returned = False
        self.period = p
        self.t_unit = tu
        self.bikes = bu
        self.shop = s
        self.customer = c
        now = datetime.now()
        c_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        if now.minute + self.period < 60:
            r_time = time(now.hour, now.minute + self.period, now.second)
        else:
            r_time = time(now.hour + 1, (now.minute + self.period) % 60, now.second)
        r_time_str = r_time.strftime("%H:%M:%S")
        # print(type(c_time))
        # print((c_time))
        self.time = now
        self.return_time = r_time
        issues.append(self)
        self.shop.stock -= self.bikes
        self.price = None


    def __str__(self):
        now = self.time
        c_time = now.strftime("%H:%M:%S")
        t_units = dict(enumerate(["Hours", "Days", "Weeks"], start = 1))

        t_units = dict(enumerate(["Hours", "Days", "Weeks"],start = 1))
        # print(t_units)
        s = str(self.customer.name) + f" has issued {self.bikes} from {self.shop.name} on {c_time} for {self.period} {t_units[self.t_unit]}."
        if self.returned:
            s += f" (issue item has been closed; customer paid ${self.price})."
        return s


    def close(self):
        self.returned = True
        self.shop.stock += self.bikes
        
        





shops = []

customers = []

issues = []



x = Rental(5, "satyam")
shops.append(x)
x = Rental(4, "raj")
shops.append(x)
x = Rental(6, "sat")
shops.append(x)



x = Customer("satyam")
customers.append(x)
x = Customer("raj")
customers.append(x)
x = Customer("sat")
customers.append(x)



# ************* Menu Pages **************



def front_page():
    print("\n\n\n\n")
    print("1. Sign-Up as owner")
    print("2. Sign-Up as customer")
    print("3. Owner Log-In")
    print("4. Customer Log-In")
    print("5. See all shops and customers")
    print("6. Exit")
    return int(input("Enter your choice: "))





def owner_login_page():
    name = input("enter username")
    for i in shops:
        if i.name == name:
            return i.front_page()
    print("no owner with given name found")


def customer_login_page():
    name = input("enter username")
    for i in customers:
        if i.name == name:
            return i.front_page()
    print("no customer with given name found")



def owner_signup_page():
    print("\n\nOwner Signup page")
    accepted = False
    while not accepted:
        name = input("Enter your desired username")
        accepted = True
        for i in shops:
            if name == i.name:
                print("Username already taken")
                accepted = False
    stock = int(input("How many bikes do you have?"))
    x = Rental(stock, name)
    shops.append(x)



def customer_signup_page():
    print("\n\Customer Signup page")
    accepted = False
    while not accepted:
        name = input("Enter your desired username")
        accepted = True
        for i in customers:
            if name == i.name:
                print("Username already taken")
                accepted = False
    x = Customer(name)
    customers.append(x)






def list_page():
    print("\nShops: ")
    for i in shops:
        print(i.name +" has bikes: "+ str(i.stock))
    print("\nCustomers: ")
    for i in customers:
        print(i.name)
    print("\nIssues: ")
    for i in issues:
        print(i)
    input()






def owner_page():
    print("\n\nOwner page")

    while True:
        print("1. To add bi-cycles stock")
        print("2. Log-out")
        c = int(input("Enter your choice: "))
        if c == 1:
            pass
        elif c== 2:
            return



def customer_page():
    print("\n\nCustomer page")

    while True:
        print("1. To issue bi-cycle")
        print("2. Log-out")
        c = int(input("Enter your choice: "))
        if c == 1:
            pass
        elif c== 2:
            return





while True:
    x = front_page()
    if x == 1:
        owner_signup_page()
    elif x == 2:
        customer_signup_page()
    elif x == 3:
        owner_login_page()
    elif x == 4:
        customer_login_page()
    elif x == 5:
        list_page()
    else:
        break


