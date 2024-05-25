#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while(i  >= 0):
        if i == 1:
            print(i) 
            print("Happy New Year!")
            break
        print(i) 
        i -= 1   
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [num * num for num in int_list]
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)    
    pass
fizzbuzz()