# 1. Date validation 32-13-2019 including leap year
# 2. Email validation for . and _
# 3. URL replacement 
# 4. Combining two files => regex 



import re

to_search = ['abc', 'text', 'match']
text = "a abc quick text brown fox jumps over the match lazy dog match, abc, text"



# to search any pattern in the given text

# x = re.search(to_search[0], text)
# if x:
#     print("found")
# else:
#     print("not found")
# print(dir(x))
# print(bool(x))
# print(dir(x))

# for i in dir(x):    
#     print(i, ": ", dir(x.__getattribute__(i)), "\n\n\n")




# split a text on the given character(s)

# st = "a"
# x = "x"
# l1 = re.split(x, text)
# l2 = re.split(st, text)

# print(l1)
# print(l2)


# # find all instances of a pattern
# y = re.findall(to_search[2], text)
# print(type(y))





# ************** video ***********

# pattern = re.compile(r'abc')

# matches = pattern.finditer(text)    # case sensitive




# for m in matches:
#     print(m)    # gives the span and match where the pattern was matched



# in regex, some meta characters ned to be escaped because these characters have special meaning in regex


# meta-characters
"""
.       - any character except new line
\d      - digits (0-9)
\D      - not a digit
\w      - any alphabet capital or small or underscores (_)
\W      - not any alphabet
\s      - whitespaces
\S      - not a whitespace 



-- anchors

\b      - word boundary i.e, the pattern is at boundary of the word like at start of word, or start of line
\B      - not a word boundary, i.e, pattern is not the start of a new word or line
^       - finds all the patterns that match the given pattern and are at the start of the main_text
$       - finds all the patterns that match the given pattern and are at the end of the main_text


"""

# characterset
"""
character set are pattern or range or set of characters that are valid to  appear at the given positions

[abcABC]        - match pattern if the character is any of a, b, c, A, B, C
[a-z]           - a to z any alphabet
[A-Z]           - A to Z 
[a-zA-Z]        - a to z or A to z
[1-5]           - 1 to 5
[^a-g]          - anything except a to g

()              - allows us to match several charsets for a position, ex. r'M(r|s|rs)' matches any pattern in the form: Mr or Ms or Mrs 



"""

# quantifiers
"""

*       - 0 or more 
+       - 1 or more
?       - 0 or 1
{3}     - exact 3
{3,6}   - min 3, max 6




"""


# ********************************************************************** PRACTICE:


# matching phone numbers:

    # to_search = ['abc', 'text', 'match']


    # text2 = """
    # a abc quick text brown fox jumps over the match lazy dog match, abc, text
    # 231.123.5434

    # 231.1232.543412
    # 2311.123.5434321
    # 231-123-54342

    # +91-6306386320

    # +91-6306386
    # +91-630638632012
    # +91-63063863200


    # """
    # text = "+91-6306386320 "


    # # phone_pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d') 
    # # phone_pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')         # using quantifiers
    # # indian_phone_pattern = re.compile(r'\+91[-][6-9]\d{9}\s')
    # indian_phone_pattern = re.compile(r'\+91[-][6-9]\d{9}(\s|$)')





    # # matches = indian_phone_pattern.finditer(text)    # case sensitive


    # # for m in matches:
    # #     print(m)    # gives the span and match where the pattern was matched

    # matches = indian_phone_pattern.search(text)    # case sensitive

    # if matches:
    #     print("valid")
    # else: 
    #     print("invalid")





# ********** email verification


    # text2 = """
    # asdasd@gasdfsa.com
    # asdasd_123123.sin@gamil.com
    # dasd1312@dfse434r3.csad
    # adadadads.comadsad
    # dfs4235r43fsdf@1224.213123



    # rules:

    # username must have aphabets, numbers, _, .,
    # @
    # mail server must have aplhabetic starting, then any aplha-numeric values
    # .
    # any aplhabetic domain name

    # """
    # text = "satyam213-webllisto.com"

    # email_pattern = re.compile(r'[a-zA-Z1-9._]{6,15}@[a-zA-Z][a-zA-Z1-9._]{3,20}\.[a-z]{,4}')
    # # email_pattern = re.compile(r'[a-zA-Z1-9._]{6,15}')

    # # matches = email_pattern.finditer(text)    # case sensitive
    # matches = email_pattern.search(text)    # case sensitive

    # if matches:
    #     print("valid")
    # else: 
    #     print("invalid")



    # # for m in matches:
    # #     print(m)    # gives the span and match where the pattern was matched











# ************** url replacement *************
    # tex = "The code is present at url www.edyoda.com/code/python or www.github.com/edyoda/python"
    # y = 'The code is present at url <a href = "www.edyoda.com/code/python">www.edyoda.com/code/python</a> or www.github.com/edyoda/python'



    # url_pattern = re.compile(r'[w]{3}\.[a-zA-Z]+\.\d{2,4}[\a-zA-Z]*')
    # url_pattern = re.compile(r'[w]{3}\.[a-zA-Z]+\.[a-zA-Z1-9]{2,4}[/a-zA-Z]*')

    # # email_pattern = re.compile(r'[a-zA-Z1-9._]{6,15}')

    # matches = url_pattern.finditer(tex)    # case sensitive
    # op = 'The code is present at url '
    # for m in matches:
    #     print(m)  # gives the span and match where the pattern was matched

    #     x = m.span()
    #     url_slice = tex[x[0] : x[1]]
    #     print(url_slice)
    #     print("\n")
    #     op +=  '<a href = "' + url_slice + '">' + url_slice + "</a> "


    # print(op)



# ******************************* pan card validation

    # tex = "MNTPS9309E"

    # # date_pattern = re.compile(r'^[A-Z]{3}[ABCFGHJLPT][A-Z]\d{4}[A_Z]$')
    # date_pattern = re.compile(r'^[A-Z]{3}[ABCFGHJLPT]+[A-Z]\d{4}[A-Z]$')


    # # print(dir(date_pattern))

    # matches = date_pattern.search(tex)    # case sensitive

    # # matches2 = date_pattern.finditer(tex)    # case sensitive


    # # print(dir(matches))
    # # print(bool(matches))
    # if matches:
    #     print("valid")
    # else:
    #     print("invalid")

    # # for m in matches2:
    # #     print(m)  # gives the span and match where the pattern was matched
    # #     x = m.span()





# ************************ combining files



    # with open("file1.txt") as f1:
    #     with open("file2.txt") as f2:
    #         n1 = f1.readline()
    #         n2 = f2.readline()

    #         f1.seek(0)
    #         f2.seek(0)
    #         print(n1)
    #         print(n2)
    #         namepattern = re.compile(r'PEP[ ][0-9]*:')

    #         m1 = namepattern.findall(n1)[0]
    #         m2 = namepattern.findall(n2)[0]

    #         m1 = m1.split()[1]
    #         m2 = m2.split()[1]
            
    #         m1 = int(m1[:-1])
    #         m2 = int(m2[:-1])
    #         with open("file3.txt", 'w') as f3:

    #             if m1 > m2:
    #                 # copy first file then second file
    #                 txt = f1.read()
    #                 print(txt.split("\n")[0])
    #                 f3.write(txt)
    #                 f3.write("\n\n")
    #                 txt2 = f2.read()
    #                 print(txt2.split("\n")[0])
    #                 f3.write(txt2)
                    
    #             else:
    #                 txt = f1.read()
    #                 print(txt.split("\n")[0])
    #                 f3.write(txt)
    #                 f3.write("\n\n")
    #                 txt2 = f2.read()
    #                 print(txt2.split("\n")[0])
    #                 f3.write(txt2)
                    
    #                 # copy second file then second file
    #                 pass
    #         # print(type(m1))
    #         # print(m2)

    #         # for m in m2:
    #         #     print(m)  # gives the span and match where the pattern was matched
    #         #     # x = m.span()
    #         # for m in m1:
    #         #     print(m)  # gives the span and match where the pattern was matched
            









# ********** date validation  ***********  skippe

tex = "29-02-2012"

date_pattern = re.compile(r'(31|30|[012][0-9])-[01]\d-\d{4}')
# date_pattern = re.compile(r'([012][0-9]|30|[12][0-9]-())(30|[12][0-9])-())-\d{4}')

# date_pattern = re.compile(r'(((31|[012][0-9])-(0[13578]|10|12))|((30|[012][0-9])-(0[469]|11)))-\d{4}')
# (31|[12][0-9])-(0[13578]|10|12)
# (30|[12][0-9])-(0[469]|11)
# email_pattern = re.compile(r'[a-zA-Z1-9._]{6,15}')

matches = date_pattern.search(tex)    # case sensitive

if matches:  
    x = matches.span()
    d = tex[x[0] : x[1]]
    print(d)
    d = d.split("-")
    y = int(d[-1])
    print(y)
    if d[0] == '29' and d[1] == "02":
        if y % 4 == 0 and y % 100 != 0:
            print("valid")
            print(matches.span())
        else:
            print("invalid 1")
    elif int(d[0]) > 29 and d[1] == "02":
        print("invalid 2")
    elif int(d[0]) == 31:
        if int(d[1]) in [1,3,5,7,8,10,12]:
            print("valid")
            print(matches.span())
        else:
            print("invalid 3")
    # elif int(d[0]) == 30 and int(d[1]) in [1,3,5,7,8,10,12]:
    #     print("valid")
    #     print(matches.span())
    else:
        print("valid")
    
else:
    print("invalid 4")




