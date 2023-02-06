'''
CMPT 395 Assignment 1
Sage Jurr
Jan. 31, 2023
Kata 1 - FizzBuzz
'''

# Requirements
# 1. write a fizzBuzz method that accepts a number as a input and returns it as a string
# 2. For multiples of 3 return Fizz
# 3. For multiples of 5 return Buzz
# 4. For multiples of 3 and 5 return FizzBuzz


# -------- NOTE TO THE MARKER ---------- #
'''
I was unsure how you wanted to track development so I decided to track each step
of fizzBuzz and the tests, I will label them by iteration so you can see the
process I take trying to implement TDD.  Sorry if this is not what you were
expecting and lots to read, if you don't want to see the process skip the
commented out fizzBuzz iterations and go to the uncommented fizzBuzz at the bottom.

Thank you!
'''

# -------------- Tests ------------- #
'''
First iteration of fizzBuzz to match criteria of acceptNum_returnString() test


def fizzBuzz():
    userInput = input("Please input a number: ")
    return userInput
'''
def acceptNum_returnString():
    output = fizzBuzz()
    
    # check if output from fizzBuzz is a string and is a number
    # This ensures that fizzBuzz is outputting a string, and that it's input was a number
    if isinstance(output, str) and output.isdigit():
        print("Test successful")
        
    else:
        print("Test Failed")
        
'''
Second iteration of fizzBuzz to match criteria of multiple3_returnFizz
Changed the userInput to a parameter for easier and faster testing.

def fizzBuzz(userInput):
    if userInput % 3 == 0:
        return "Fizz"
    else:
        return
'''
def multiple3_returnFizz():
    # check if multiple of 3 is inputted into fizzBuzz it should return Fizz
    # If it doesn't then it is a failure
    
    
    # First input 3 into fizzBuzz this should return fizz
    output = fizzBuzz(3)
    if output == "Fizz":
        print("Test Successful")
        
    else:
        print("Test Failed")
        
    
    # Now input 19 which is not a multiple of 3 so it should return nothing
    output = fizzBuzz(19)
    if output == None:
        print("Test Successful")
        
    else:
        print("Test Failed.")
             
'''
Third iteration of fizzBuzz

def fizzBuzz(userInput):
    if userInput % 3 == 0:
        return "Fizz"
    elif userInput % 5 == 0:
        return "Buzz"
    else:
        return
'''

def multiple5_returnBuzz():
    # check if multiple of 5 is inputted into fizzBuzz it should return Buzz
    # If it doesn't then it is a failure
    
    
    # First input 5 into fizzBuzz this should return Buzz
    output = fizzBuzz(5)
    if output == "Buzz":
        print("Test Successful")
        
    else:
        print("Test Failed")
    
    multiple3_returnFizz() # ensures previous tests still pass
           
'''
Fourth iteration of fizzBuzz FINAL WORKING FUNCTION
'''
def fizzBuzz(userInput):
    if userInput % 3 == 0 and userInput % 5 == 0:
        return "FizzBuzz"
    if userInput % 3 == 0:
        return "Fizz"
    elif userInput % 5 == 0:
        return "Buzz"
    else:
        return

def multiple3And5_returnFizzBuzz():
    # check if multiple of 3 and 5 is inputted into fizzBuzz it should return FizzBuzz
    # If it doesn't then it is a failure
    
    # First input 15 into fizzBuzz which is a multiple of 3 and 5 it should return FizzBuzz
    output = fizzBuzz(15)
    if output == "FizzBuzz":
        print("Test Successful")
        
    else:
        print("Test Failed")    
    
    multiple5_returnBuzz() # ensures previous tests still pass

multiple3And5_returnFizzBuzz()