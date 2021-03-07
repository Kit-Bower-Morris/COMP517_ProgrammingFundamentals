# Kit Bower-Morris
# Student Number: 201532917
# COMP517 - CA3


# Global scope lists called "cache" and "requests".
cache = []
requests = []


# Menu function. 
# Ask user to request integers, enter 0 to stop requesting.
# Check that input can be converted to an int, if not show error message and ask user to try again. 
# Prints options. Asks user to input which option they want. 
# If q is selected, quit program. 
# If a input is wrong, return to menu().
# If statement to call selected option.
def menu():
    print("\n***Main Menu***")
    print("Please repeatly request integers, to finish requesting enter '0'")
    
    req = input("Please enter an integer: ")
    while (req != "0"):
        if(req.isdigit()):
            req = int(req)
            requests.append(req)
        else:
            print("Sorry please only enter integers!")
        req = input("Please enter an integer: ")

    print("\nWhich managment technique would you like?\n")
    print("Option 1: First in first out - the request that has been present in the cache the longest will be removed")
    print("Option 2: Least Frequently used - the least requested integer in cache will be removed")
    print("Option q: Exit the program.") 
    
    opt = (input("\nPlease type either '1', '2' or 'q' to select that corrisponding option: "))
    
    if(opt == "q"):
        print("Option q: Exit the program.")
        print("\nExiting program. Goodbye!\n")
        exit()
    elif(opt == "1"):
        print("Option 1: First in first out") 
        fifo()
    elif(opt == "2"):
        print("Option 2: Least Frequently used")
        lfu()
    else:
        print("\nError wrong input! Please try again!")
        menu()


# First in first out function.
# If item is already in cache print 'Hit'.
# Otherwise print 'Miss' and check to see if cache has less than 8 elements, if so append item to cache.
# If cache is full, delete the element at index [0], then append the new request. 
# Print the contents of the cache.
# Clear the cache and the requests. 
# Return to the main menu.
def fifo():
    for item in requests:
        if(item in cache):
            print("Requesting page: ", item , " Hit")
        else:
            print("Requesting page: ", item , " Miss")
            if(len(cache)<=7):
                cache.append(item)
            else:
                del cache[0]
                cache.append(item) 
    print("Cache = ", cache)
    cache.clear()
    requests.clear()
    menu()         


# Least frequently used function. 
# Create a list called log, which records the hits for the indexes in the cache.
# If item is in cache, print 'Hit' and determine its index. Then add one to element at the same index in log.
# If item is not in cache, print 'Miss' and check to see if cache has less than 8 elements, if so append item to cache.
# Otherwise determine the least frequently used elements. Create a list with these elements indexes.
# Use these indexes to create another list with the values in cache with the same corrisponding indexes.
# Find the minimum value of this list which contains all the least frequently used pages. 
# Remove this element from cache, replacing it with the new request.
# Remove the corrisonding element from log, replacing it with 0.
# Print the contents of the cache.
# Clear the cache and the requests. 
# Return to the main menu.  
def lfu():
    log = [0,0,0,0,0,0,0,0]
    for item in requests:
        if(item in cache):
            print("Requesting page: ", item , " Hit")
            position = cache.index(item)
            count = log.pop(position)
            count = count + 1
            log.insert(position, count)      
        else:
            print("Requesting page: ", item , " Miss")
            if(len(cache)<=7):
                cache.append(item)
            else:
                logIndex = []
                cacheValue = []
                least = min(log) 
                for i in range(0, len(log)): 
                    if log[i] == least : 
                        logIndex.append(i)
                for i in range(0, len(logIndex)): 
                    x = logIndex[i]
                    x = cache[x]               
                    cacheValue.append(x)
                least = min(cacheValue)
                least = cache.index(least)              
                del cache[least]
                cache.insert(least, item)
                del log[least]
                log.insert(least, 0)
    print("Cache = ", cache)
    cache.clear()
    requests.clear() 
    menu()         


# Call menu function. 
menu()