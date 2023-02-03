'''
CMPT 395 Assignment 1
Sage Jurr
Feb. 2, 2023
Kata 2 - Point of Sale
'''

# -------- NOTE TO THE MARKER ---------- #
'''
I was unsure how you wanted to track development so I decided to track each step
of POS() and total(), I will label them by iteration so you can see the
process I take trying to implement TDD.  Sorry if this is not what you were
expecting and lots to read, if you don't want to see the process skip the
commented out POS iterations and go to the uncommented fizzBuzz at the bottom.

Thank you!
'''

# - A note with my tests, the test function checks that the output is correct I visually confirm it is printing the correct display from POS - #

'''
First iteration of POS

def POS(barcode):
    # Note returns a float so easier for totalling later
    if barcode == '12345':
        print('The price of ' + barcode + ' is $' + str(7.25) + '.')
        return 7.25
    
    else:
        return
'''    
def accept12345_return725():
    # Tests that if POS gets '12345' as a barcode it returns 7.25
    # and if not returns None
    output = POS('12345')
    if output == 7.25:
        print("Test Successful")
        
    else:
        print("Test Failed")
        
    output = POS('3456')
    if output == None:
        print("Test Successful")
        
    else:
        print("Test Failed")
        
'''
Second iteration of POS

def POS(barcode):
    # Note returns a float so easier for totalling later
    if barcode == '12345':
        print('The price of ' + barcode + ' is $' + str(7.25) + '.')
        return 7.25 
    elif barcode == '23456':
        print('The price of ' + barcode + ' is $' + str(12.50) + '.')
        return 12.50
    else:
        return
'''    
def accept23456_return1250():
    accept12345_return725() # ensures previous tests still work with new function
    output = POS('23456')
    if output == 12.50:
        print("Test Successful")
        
    else:
        print("Test Failed")    


'''
Third iteration

def POS(barcode):
    # Note returns a float so easier for totalling later
    if barcode == '12345':
        print('The price of ' + barcode + ' is $' + str(7.25) + '.')
        return 7.25 
    elif barcode == '23456':
        print('The price of ' + barcode + ' is $' + str(12.50) + '.')
        return 12.50
    elif barcode == '99999':
        print('Error: barcode not found')
        return   
    else:
        return
'''

def accept99999_returnError():
    accept23456_return1250() # ensures previous tests still work
    print()
    output = POS('99999')
    if output == None:
        print("Test Successful")
        
    else:
        print("Test Failed")    

'''
Fourth iteration
'''
def POS(barcode):
    # Note returns a float so easier for totalling later
    if barcode == '12345':
        print('The price of ' + barcode + ' is $' + str(7.25) + '.')
        return 7.25 
    elif barcode == '23456':
        print('The price of ' + barcode + ' is $' + str(12.50) + '.')
        return 12.50
    elif barcode == '99999':
        print('Error: barcode not found')
        return
    elif barcode == '':
        print('Error: empty barcode')
        return       
    else:
        return


def acceptEmpty_returnError():
    accept99999_returnError()
    print()
    output = POS('')
    if output == None:
        print("Test Successful")
        
    else:
        print("Test Failed")    
        
'''
First iteration of total

def total():
    total = 0
    numItems = input("How many items to scan?")
    for i in range(int(numItems)):
        barcode = input("Enter barcode: ")
        output = POS(barcode)
        if output == None:
            pass
        else:
            total += output
    print("The total owed is: " + str(total))
'''

def TestTotalCorrect():
    # manually enter in 4 items to scan
    # Then enter 12345 and 23456 and 99999 and ''
    # ensure calculated total is 19.75
    total()
    
'''
Second iteration of total
'''
def total():
    # in this iteration making it more readable to the user
    total = 0
    numItems = input("How many items to scan? ")
    for i in range(int(numItems)):
        barcode = input("Enter barcode: ")
        output = POS(barcode)
        print()
        if output == None:
            pass
        else:
            total += output
    print("The total owed is: " + str(total))
    
#TestTotalCorrect()      