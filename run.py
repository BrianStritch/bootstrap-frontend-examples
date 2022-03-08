import math
from datetime import datetime

max_guests = 60
guests_per_table = 6
available_tables = 10
availability = True
remaining_seats = 60

def intro():
    global remaining_seats
    num_of_guests = int(input('how many guests do you have:'))
    while num_of_guests >= remaining_seats:
        print('no availability left for a group that size')
        num_of_guests = int(input('how many guests do you have 2:'))
    else:        
        return num_of_guests


def num_of_tables(num_of_guests):
    tables = math.ceil(num_of_guests/6)
    print('number of tables:', tables)
    return tables

def capacity(tables):
    in_house = tables * 6
    print('in house diners = ',in_house)
    return in_house
    
    
def remaining_guest_spaces(in_house):
    global remaining_seats
    remaining_seats -= in_house
    print('remaining seats = ', remaining_seats )

    return remaining_seats
    


def remaining_tables(remaining_seats):
    global available_tables
    global availability
    available_tables =  math.floor(remaining_seats / 6)    
    print('new available tables = ', available_tables)
    if available_tables > 1:
        print('in while loop return true')
        availability = True
        print('date today =', datetime.now())
    else:
        print('in while loop return false')
        availability = False






def booking():
    while availability:
        guests = intro()
        tables = num_of_tables(guests)
        in_house = capacity(tables)
        remaining_seats = remaining_guest_spaces(in_house)
        remaining_tables(remaining_seats)

    else:
        print('restaurant is now closed')

def main():
    booking()
    

#main()

