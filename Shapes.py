# Kit Bower-Morris
# Student Number: 201532917
# COMP517 - CA1

#Main Menu.
def menu():
#Print Main Menu text.
    print("\n***Main Menu***\n")
    print("Option 1: Calculate unknown angle for a triangle with two known angles.")
    print("Option 2: Calculate the length of the hypotenuse side of a right-angle triangle with both other side lengths known.")
    print("Option 3: Calculate the area of a triangle when all three side lengths are known.") 
    print("Option q: Exit the program.") 
    answer = (input("\nPlease type either '1', '2', '3' or 'q' to select that corrisponding option: "))
#If statements to call relevent function depending on the input.
    if(answer == "1"):
        optAngle()
    elif(answer == "2"):
        optLength()
    elif(answer == "3"):
        optArea() 
    elif(answer == "q"):
        print("\nExiting program. Goodbye!\n")
#If user enters wrong value, print error message and return to menu.   
    else:
        print("\nError wrong input! Please try again!")
        menu()

#Option 1.
def optAngle():
#Ask user for inputs, converting them to floats..
    angleA = float(input("\nPlease enter the size (degrees) of the first known angle: "))
    angleB = float(input("Please enter the size (degrees) of the second known angle: "))
#Calculate third angle. Angles in a triangle add up to 180. 
    angleC = 180-angleA-angleB
#Print error if the inputs cannot create a triangle. Angle C cannot be less than or equal to 0.
    if(angleC<=0):
        print("\nError! Impossible Triangle! One or more of entered angles was too large!\n")
#Otherwise print results for all three angles. "%.2f" % gives the angles to two decimal points. 
    else:
        print("\nThe size of the unknown angles is:")
        print(("%.2f" % angleC), "degrees.") 
        print("\nTherefore the sizes of the three angles of the triangle are:")
        print(("%.2f" % angleA), "degrees,", ("%.2f" % angleB), "degrees and", ("%.2f" % angleC), "degrees.")
#Return to main menu. 
    menu()

#Option 2.
def optLength():
#Ask user for inputs, converting them to floats.
    lengthA = float(input("\nPlease enter the length of first known side (cm): "))
    lengthB = float(input("Please enter the length of second known side (cm): "))
#Calculate length of third side. For right-angled triangles this is done through Pythagoras' theorem: (a**2)+(b**2)=(c**2). (x**0.5 finds the square root).
    lengthC = ((lengthA**2)+(lengthB**2))**0.5
#Print results, giving lengths of all three sides. 
    print("\nThe hypotenuse is length: ")
    print(("%.2f" % lengthC), "CM.")
    print("\nTherefore the three sides are length:")
    print(("%.2f" % lengthA), "CM,", ("%.2f" % lengthB), "CM and", ("%.2f" % lengthC), "CM.")
#Return to main menu.
    menu()

#Option 3.
def optArea():
#Ask user for inputs, converting them to floats..
    lengthA = float(input("\nPlease enter the length of first known side (cm): "))
    lengthB = float(input("Please enter the length of second known side (cm): "))
    lengthC = float(input("Please enter the length of third known side (cm): "))
#Follow Heron's Formula for the area of a triangle. First find the value of half the perimeter. ((a+b+c)/2).
    halfPer = (lengthA+lengthB+lengthC)/2
#If half the perimeter is smaller or equal to one or more of the lengths then give an error as this would be an impossible triangle.
    if(halfPer<=lengthA or halfPer<=lengthB or halfPer<=lengthC):
        print("\nSorry! Impossible triangle!")
#Otherwise continue with Heron's Formula. If p is equal to half the perimeter then the area of the triangle is the square root of p(p-a)(p-b)(p-c).
    else:
        area = (halfPer*(halfPer-lengthA)*(halfPer-lengthB)*(halfPer-lengthC))**0.5
        print("\nArea of the triangle is:")
        print(("%.2f" % area), "CM^2")
#Return to main menu.
    menu()

#Call Main Menu.
menu()