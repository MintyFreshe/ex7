"""A template for a python script deliverable for INST326.

Driver: Nathaniel Minty, Yaniv Ashwal
Navigator: Nathaniel Minty, Yaniv Ashwal
Assignment: ex 7
Date: 4_8_25

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import re




class Address:

    def __init__(self, street, city, state):
    
        self.street = street

        self.city = city

        self.state = state





class Employee:

    def __init(self, row):

        
        tuple_return = parse_name(row)
        
        
        first_name = tuple_return[0]

        last_name = tuple_return[1]

        address = parse_address(row)

        email = parse_email(row)





def parse_name(text):

    
    




    return #tuple (first, last)



def parse_address(text):

    #regex street city state 



    
    
    addressobj = Address(street, city, state)

    return addressobj



def parse_email(text):

    #regex email



    return #email



def main(path):
    
    #open read and separate lines
    
    openfile = open(path, 'r') 
    
    
    file_as_string = openfile.readlines()

    
    lines = file_as_string.splitlines()
    
    
    employee_list = []
    
    
    for text in lines:

        Employeex = Employee(text) #<- employeex is a placeholder for the employee name or employee number
                
    
       
    
    
    return(employee_list)



if __name__ == "__main__":
  
    main(path) #????? 
