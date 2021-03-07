# Kit Bower-Morris
# Student Number: 201532917
# COMP517 - CA2

#Menu function. 
#Prints options. Asks user to input which option they want. 
#If q is selected, quit program. 
#If a input is wrong, return to menu().
#If statement to print selected option.
#Call menu2 function.
def menu():
    print("\n***Main Menu***")
    print("Option 1: Calculate the sum of two numbers.")
    print("Option 2: Calculate the product of two numbers.")
    print("Option 3: Raise one number to the power of the other.") 
    print("Option 4: Calculate the remainder between two numbers.")
    print("Option q: Exit the program.") 
    opt = (input("\nPlease type either '1', '2', '3', '4' or 'q' to select that corrisponding option: "))
    if(opt == "q"):
        print("Option q: Exit the program.")
        print("\nExiting program. Goodbye!\n")
        exit()
    elif(opt != "1" and opt != "2" and opt != "3" and opt != "4"):
        print("\nError wrong input! Please try again!")
        menu()
    else:
        if(opt == "1"):
            print("Option 1: Calculate the sum of two numbers.")
        elif(opt == "2"):
            print("Option 2: Calculate the product of two numbers.")
        elif(opt == "3"):
            print("Option 3: Raise one number to the power of the other.")
        else:
            print("Option 4: Calculate the remainder between two numbers.")
        menuTwo(opt)

#MenuTwo is a seperate function so that user's option choice is retained if user inputs a number in a wrong range for option selected. 
# Zero is not positive. 
#Ask user to input two numbers. Assign them as floats. 
#If statements seperated by what option the user selected. 
#Ensure the numbers input by the user align with the ranges of the option selected. If they are not within the range, allow the user to input two new numbers, by calling menuTwo again by retaining value of opt. 
#Each option then calls corrispoding fuction, inserting the users two numbers.
#Check if the returned value from fuction is an integer or not. If it is and the numbers submitted by user are also integers, then print results as integers. 
#Otherwise print results as floats.
#Return user to the main menu (menu()). 
def menuTwo(opt):
    
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))    
    
#option one has no limits to range. 
    if(opt == "1"):
        ans = sum(x,y)
        if(ans.is_integer() and x.is_integer() and y.is_integer()):
            print(int(x), "+", int(y), "=", int(ans))
        else:
            print(x, "+", y, "=", ans)

#option two have to be positive and the second inputted number must be an integer.
    elif(opt == "2"):
        if(float(y)<=0 or float(x)<=0):
            print("\nSorry please enter positive numbers!\n")
            menuTwo(opt)
        elif(y.is_integer()):
            ans = prod(x,y)
            if(ans.is_integer() and x.is_integer() and y.is_integer()):
                print(int(x), "*", int(y), "=", int(ans))
            else:            
                print(x, "*", y, "=", ans)
        else:
            print("\nSorry second number must be a positive integer!\n")
            menuTwo(opt)

#option three inputs must be positive integers.
    elif(opt == "3"):
        if(int(y)<=0 or int(x)<=0):
            print("\nSorry please enter POSITIVE integers!\n")
            menuTwo(opt)
        elif(x.is_integer() and y.is_integer()):
            x = int(x)
            y = int(y)
            ans = exp(x,y)
            print(x, "^", y, "=", ans)          
        else:
            print("\nSorry please enter positive INTEGERS!\n")
            menuTwo(opt) 

#option four inputs must be positive. 
    else:
        if(float(y)<=0 or float(x)<=0):
            print("\nSorry please enter positive numbers!\n")
            menuTwo(opt)
        else:
            ans = modulo(x,y)            
            if(ans.is_integer() and x.is_integer() and y.is_integer()):
                print(int(x), "%", int(y), "=", int(ans))
            else:            
                print(x, "%", y, "=", ans)  
    
    menu()

#Sum function. Adds the two inputs together. 
#Returning the result. 
def sum(x,y):
    ans = x + y
    return ans

#Prod function. Runs sum function, plusing x to itself y times.
#Returning the result.
def prod(x,y):
    count = 0
    ans = 0 
    while(count < y):
        ans = sum(ans,x)
        count = count + 1
    return ans

#Exp function. 
#x^1 = x. 
#Call prod(x,x) to find the square of x. Then if y is larger than 2, using a for loop, mulitply the square of x by x (y-2) times.
#Returning the result. 
def exp(x,y):              
    if(y == 1):
        return x
    else:
        ans = prod(x,x)
        for i in range(2,y):
            ans = prod(ans,x)
    return ans

#Negate y.
#Call sum() in a while loop until result is smaller or equal to positive y. 
#Returning the result.  
def modulo(x,y):
    y = -y
    while(x>=-y):
        x = sum(x,y)
    return x

#Call menu function. 
menu()