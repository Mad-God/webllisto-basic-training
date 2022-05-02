# Question 1 *************************************
"""

    ip = input()

    alphas = [['a','b','c'],['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

    def numbers_to_chars(str):
        op = ""
        p = str[0]
        count = 0
        for i in str[1:]:
            if i == p:
                # print("in the if: ",i, count)77772899926
                count+=1
            else:
                # print(i, count)
                op += alphas[int(p) -2 ][count]
                p = i
                count = 0
        # print(i, count)

        op += alphas[int(p) -2 ][count]
        print(op)

    numbers_to_chars(ip)

"""

# Question 2 *************************************


"""
    dest = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}
    def travel_sequence(dest):
        fr = set(dest.keys())
        to = set(dest.values())

        origin = fr.difference(to)
        # print(origin)
        origin = origin.pop()
        # print(type(origin))
        op = ""
        while origin in dest:
            op += origin+"->"+str(dest[origin])+","
            origin = dest[origin]
        return op
    print(travel_sequence(dest))

"""



# Question 3 **************************************

"""
    states = {'New Hampshire': ['Concord', 'Hanover'],

    'Massachusetts': ['Boston', 'Concord', 'Springfield'],

    'Illinois': ['Chicago', 'Springfield', 'Peoria'] }

    def city_map(states):
        cl = list(states.values())

        cities = list(item for sublist in cl for item in sublist)
        cities = set(cities)
        cities = list(cities)
        cmap = {}
        cmap = cmap.fromkeys(cities, [])
        # print("cmap: ",cmap)

        for i in cmap:
            cmap[i] = []


        for c in cities:
            # print("current city c in the outer loop:cls",c)
            for i,j in states.items():
                # print("i, j: ", i, j)
                if c in j:
                    # print("c, j in the loop: ",c, j)

                    # print("cmap[c]", cmap[c])
                    if i not in cmap[c]:
                        cmap[c].append(i)
                    # print("cmap in the loop: ", cmap)


        print(cmap)
        return cmap



    city_map(states)

"""


# Question 4 *************************************

"""

    def check_parenthesis(s):
        cir = 0
        squ = 0
        cur = 0
        bt = []
        for i in s:
            print(i)
            if i == "(":
                # cir += 1
                bt.append(i)
            elif i == ")":
                # cir -= 1
                if len(bt) > 0 and bt[-1] == "(":
                    bt.pop(-1)
                else:
                    return False
            elif i == "[":
                # squ += 1
                bt.append(i)
            elif i == "]":
                # squ -= 1
                if len(bt) > 0 and bt[-1] == "[":
                    bt.pop(-1)
                else:
                    return False
            elif i == "{":
                # cur += 1
                bt.append(i)
            elif i == "}":
                # cur -= 1
                if len(bt) > 0 and bt[-1] == "{":
                    bt.pop(-1)
                else:
                    return False
            else:
                pass
                print("i: ", i)
            print(bt)

            # if cir < 0 or squ < 0 or cur < 0:
                # return False
        print(bt)
        if len(bt) == 0:
            return True
        else:
                return False

    print(check_parenthesis(r"()[]{{]}}"))

"""







# Question 5 *************************************

"""
    num = 999

    def int_to_roman(num):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        rev_rom = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        nums = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        s = ""
        while num > 0:
            digs = num//nums[i]
            num %= nums[i]
            while digs:
                s += sym[i]
                digs -= 1
            i -= 1
        return s    

    print(int_to_roman(num))


"""





# Question 6 *************************************

"""
    def func(s):
        ls = s.splitlines()
        # print(ls)
        count =0
        for i in ls:
            # print(count)
            # print(repr(i))
            if i.isspace() or i.startswith("#") or i == "":
                pass
            else:
                # print(i)
                count +=1
        pass
        return count
   
    s = ""
    #Linear search implementation
    #Takes list and a key as input and returns True or False as answer
    def linear_saerch(l,key):
        for value in l:
            if key == value:
                return True #Return True is key exist
        else:
            return False #Return False if key does not exist

    l = [100,200,300,400,500,600]
    key = 500
    result = linear_search(l,key)
    print(result)
    ""
    print(func(s))

"""





# Question 7 ************************************
"""
    pwd = "asdasd2A@"

    def pwd_strength(pwd):
        
        errors = []

        if len(pwd) < 8:
            errors.append("Length less than 8 characters")
        has_spe = False
        has_num = False
        has_cap = False
        for c in pwd:
            if c.isupper():
                has_cap = True
            if c.isdigit():
                has_num = True
            if c in ['!','@','#','$','&']:
                has_spe = True
        if not has_spe:
            errors.append("No special Characters")
        if not has_num:
            errors.append("No Numeric Characters")
        if not has_cap:
            errors.append("No Capital Letter Characters")
        if len(errors) == 0:
            return "Strong Password"
        return "Weak password", errors

    print(pwd_strength(pwd))

"""





# Question 7 b *********************************
"""
    s = "A quick brown fox jumps over the lazy dog."

    def check_sen(s):
        errors = []
        if not s[0].isupper():
            errors.append("First alphabet not Capital.")
        if not s[-1] == ".":
            errors.append("Does not end with full stop")
        for i in range(len(s)):
            if s[i] == " ":
                if s[i+1] == " ":
                    errors.append("Two consecutive spaces at {} postion.".format(i))
            if s[i].isupper():
                if s[i+1].isupper():
                    errors.append("Two consecutive capital letters at {} postion.".format(i))
            
        if len(errors) == 0:
            return "Syntactically Correct"
        return "Syntactically Incorrect", errors




    print(check_sen(s))

"""






# Question 8 ************************************
"""
    lst = [1, 4, 3, 2, 5]


    def greatest_sub_array(lst, k):
        all_subs = []
        i = 0
        j = k
        while j <= len(lst):
            all_subs.append(lst[i:j])
            i += 1
            j += 1
        print(all_subs)
        ans = all_subs[0]
        for sub in all_subs:
            broken = False
            i = 0
            while i < k:
                if ans[i] < sub[i]:
                    print("ans,sub, i", ans,sub, i)
                    ans = sub
                    broken = True
                    break
                i += 1
            print("ans: ", ans)
            if broken:
                break
        return ans


    print(greatest_sub_array(lst, 1))

"""



# Question 9 *************************************
"""
    lst = [1, 3, 5, 4, 2]

    def adj_sum_even(lst):
        e = 0
        o = 0
        for i in lst:
            if i % 2 == 0:
                e += 1
            else:
                o += 1
        if e > o:
            return o
        else:
            return e


    print(adj_sum_even(lst))

"""




# Question 10 ************************************
"""
    def ret_sum(a,b):
        if a == b:
            return 2*(a+b)
        return a+b
    print(ret_sum(2,2))
"""


# Question 11 ************************************
"""
    def calc_pr_ls(cp, sp):
        diff = abs(sp-cp)
        pr = (diff/cp)*100
        ans = ""
        print(diff)
        if cp > sp:
            ans = "profit"
        else:
            ans = "loss"
        return pr, ans

    print(calc_pr_ls(290,230))
"""




# Question 12 ************************************
"""
    sal = int(input())

    def cal_sal(sal):
        if sal <= 10000:
            hra = sal / 5
            da = (sal*8)/10
            gs = sal + hra + da
            return gs
        elif sal <=20000:
            hra = sal/4
            da = (sal*9)/10
            gs = sal + hra + da
            return gs
        else:
            hra = (3*sal)/10
            da = (sal*95)/100
            gs = sal + hra + da
            return gs

    print(cal_sal(sal))

"""




# Question 13 ************************************
"""
    year = 2004

    def isLeap(year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    print(isLeap(year))
"""



# Question 14 ***********************************

"""
    a = 12
    b = 11
    c = 13

    def triCheck(a,b,c):
        if a == b and b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else: 
            return "Scalene"


    print(triCheck(a,b,c))

"""



