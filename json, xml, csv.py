
# # **************** jSON ***********************
# # json: java script object notation


# # '''
# # Conversion table:

# # object -> dict
# # array -> list
# # string -> str
# # number(int) -> int
# # number(real) -> float
# # null -> None 

# # '''

# from urllib.request import urlopen
# import json


# dummy_json = """
# {
#   "states": [
#     {
#       "name": "Colorado",
#       "abbreviation": "CO"
#     },
#     {
#       "name": "Connecticut",
#       "abbreviation": "CT"
#     },
#     {
#       "name": "Delaware",
#       "abbreviation": "DE"
#     },
#     {
#       "name": "Florida",
#       "abbreviation": "FL"
#     },
#     {
#       "name": "Georgia",
#       "abbreviation": "GA"
#     },
#     {
#       "name": "Hawaii",
#       "abbreviation": "HI"
#     }
#   ]
# }
# """



# # load the data from a string
# data = json.loads(dummy_json)


# print(data)

# # dumps the data into a json string
# new_json = json.dumps(data, indent = 2, sort_keys=True)


# # print((new_json))

# data = json.loads('''{
#   "states": [
#     {
#       "name": "Alabama",
#       "abbreviation": "AL",
#       "area_codes": ["205", "251", "256", "334", "938"]
#     },
#     {
#       "name": "Alaska",
#       "abbreviation": "AK",
#       "area_codes": ["907"]
#     },
#     {
#       "name": "Arizona",
#       "abbreviation": "AZ",
#       "area_codes": ["480", "520", "602", "623", "928"]
#     },
#     {
#       "name": "Arkansas",
#       "abbreviation": "AR",
#       "area_codes": ["479", "501", "870"]
#     },
#     {
#       "name": "California",
#       "abbreviation": "CA",
#       "area_codes": ["209", "213", "310", "323", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "628", "650", "657", "661", "669", "707", "714", "747", "760", "805", "818", "831", "858", "909", "916", "925", "949", "951"]
#     },
#     {
#       "name": "Colorado",
#       "abbreviation": "CO",
#       "area_codes": ["303", "719", "720", "970"]
#     },
#     {
#       "name": "Utah",
#       "abbreviation": "UT",
#       "area_codes": ["385", "435", "801"]
#     },
#     {
#       "name": "Vermont",
#       "abbreviation": "VT",
#       "area_codes": ["802"]
#     },
#     {
#       "name": "Virginia",
#       "abbreviation": "VA",
#       "area_codes": ["276", "434", "540", "571", "703", "757", "804"]
#     },
#     {
#       "name": "Washington",
#       "abbreviation": "WA",
#       "area_codes": ["206", "253", "360", "425", "509"]
#     },
#     {
#       "name": "West Virginia",
#       "abbreviation": "WV",
#       "area_codes": ["304", "681"]
#     },
#     {
#       "name": "Wisconsin",
#       "abbreviation": "WI",
#       "area_codes": ["262", "414", "534", "608", "715", "920"]
#     },
#     {
#       "name": "Wyoming",
#       "abbreviation": "WY",
#       "area_codes": ["307"]
#     }
#   ]
# }''')


# with open('states.json', 'w') as js:
#     json.dump(data, js, indent = 2, separators = (", ", ": "))




# with open('states.json') as js:
#     data = json.load(js)


# print(data)



# for d in data["states"]:
#     print("asdaddas")
#     print(d)



# with urlopen(r"https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read() 

# data = json.loads(source)
# print(data)


# *********************************************



# *************** XML *************************
# xml: extansible markup language

# general format:
    # <?xml version="1.0" encoding="sdad">
    # <metadata>
        # actual data in form of tags
    # </metadata>



# paring modules:
    # element tree formats data in a tree structure
    # mini.dom parses XML into DOM

# ******** parsing data 
import xml.etree.ElementTree as ET

mytree = ET.parse("sample.xml")

# mytree = ET.fromstring(data)                  # to parse a string as an xml file

myroot = mytree.getroot()           # now my root in an element object with attributes like tag, attrib, text etc




# ******** finding data 

print(myroot[0].attrib)             # to get the dict of attributes of the first child of the myroot element tag

for i in myroot[0]:                 # iteration is done on the child elements of the current element
    print(i)


for i in myroot.findall("book2"):
    print(i.attrib["id"])
    print("sdasddsa ",i)
    print(i.text, end = "")
    print(i.find("price").text)



# ******** modifying data 

# u can iterate over the elements, and modify their text, attributes as such:

for i in myroot:
    print(i)
    print(i.attrib)
    i.attrib = {"new": "val"} # to update the whole atrribute dict
    i.set("set", "val2") # to add just a new attrib
    i.attrib.pop("set") # remove an attrib using the pop method

print("\n\n")
for i in myroot:
    print(i.attrib)
    


# to remove an element from the tree, we have to pass its reference to the remove() method on the parent Element object

for child in myroot:
    print(child.tag)
    if child.name != "prop":
        continue
    if True: # TODO: do your check here!
        myroot.remove(child)




# all this data is still in python but the xml file is not updated, so we must write it back to the original or a new xml file
# mytree.write("new.xml")


# from xml.dom import minidom

# mytree = minidom.parse("sample.xml")

# c1 = mytree.getElementsByTagName("book2")
# print(c1)

# for i in c1:
#     print(i)
#     print("Sdasdads")
#     print(i.firstChild.data)




# *********************************************



# ****************** CSV **********************

# CSV: Comma separated values

import csv
from operator import delitem

with open("Customer.csv") as csvf:
    file_name = csv.reader(csvf)
    print(file_name)

    # read file record by record
    for line in file_name:
        print(line)

    with open("newcsv.csv", 'w') as newf:
        writer = csv.writer(newf)

        for line in file_name:
            print("asdadsadsaA")
            writer.writerow(line)

    file_name = csv.DictReader(csvf)
    print(file_name)

    # read file record by record
    for line in file_name:
        print(line)

    with open("newcsv.csv", 'w') as newf:
        writer = csv.DictWriter(newf, fieldnames=["CustomerID", "Name", "Cluster", "Genre", "Age", "Annual Income (k$)", "Spending Score (1-100)"],
            delimiter = ",")
        
        writer.writeheader()

        writer.writerows(file_name)
        for line in file_name:
            print("asdadsadsaA")
            writer.writerow(line)
        print(newf)



# json combining 2 wfiles, xmls xmltodictreader, iterator, generator, 
# *********************************************

