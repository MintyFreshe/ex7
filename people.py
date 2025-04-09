"""Regex practice script using the people.txt file for data to pull from

Driver: Nathaniel Minty, Yaniv Ashwal
Navigator: Nathaniel Minty, Yaniv Ashwal
Assignment: ex 7
Date: 4_8_25

Challenges Encountered: formatting the Regex, returning in desired format
"""


import re

class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
        
    def __repr__(self):
        return f"Address(street='{self.street}', city='{self.city}', state='{self.state}')"



class Employee:
    def __init__(self, row):
        name = parse_name(row) #tuple of (firstname, lastname)
        self.first_name = name[0] 
        self.last_name = name[1]
        self.address = parse_address(row) 
        self.email = parse_email(row)

    def __repr__(self): # to represent text nice(ish)ly. we could fix that with pandas though.
        return (f"Employee(first_name='{self.first_name}', last_name='{self.last_name}', " +
                f"address={self.address}, email='{self.email}")


def parse_name(text):
    pattern = r"^([A-Z][a-z]+)\s([A-Z][a-z]+)"
        #name starts with uppercase, continues lowercase.
    match = re.search(pattern, text)
    if match:
        return match.group(1), match.group(2) #tupleify
    return None #if no match



def parse_address(text):
    pattern = r'(\d+.*?)\b(\w+\s)([A-Z]{2})'
        
    match = re.search(pattern, text)
    if match:
        street = match.group(1)
        city = match.group(2)
        state = match.group(3)
    else: 
        return None #if no match 
    
    address = Address(street, city, state)

    #print(f"Address: {address}") #debugging line to see if the address is being parsed correctly

    return address



def parse_email(text):
    pattern = r"[\w._%+-]+@[a-zA-Z]+\.[a-zA-z]+"
            #alphanumeric withsigns - @ - domainname -  'dot' - Top Level Domain
    match = re.search(pattern, text)
    if match: 
        return match.group()
    return None



def main(path):
    with open(path, 'r') as file:  
        file_text = file.readlines() 
    
    employee_list = []
    
    for line in file_text: 
        employee_list.append(Employee(line))

        
    return(employee_list)



if __name__ == "__main__":
    result = main("people.txt")
    print(result)
