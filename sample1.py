"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Section: Tuesday, CMPS 1501-05 11-12.15 pm
    Assignment: lab6pr1.py
    Date: 10/29/2018
    Program to take input from a file containing a list of numbers, one number per line, and check if they are in
    increasing order. Includes big Oh analysis.
"""

def is_file_sorted(filename):
    """ (str)-> int->Bool
    >>>>['4\n', '5\n', '6\n', '7\n', 8\n']
    True
    >>>>['4\n', '3\n', '29\n', '0\n', '7\n']
    False
    >>>>['-12\n', '0\n', '21\n', '100\n']
    True
    >>>>['25\n', '-75\n', '1\n', '2\n', '3\n']
    False
    >>>>['7\n']
    True
    """
    #Reads contents of file into list of strings
    
    f = open(filename, 'r')     #O(1) + O(1) = O(2) = O(1)
    lst = f.readlines()         #O(N)
    f.close()                   #O(1)

    #converts string elements to integers and compares values.
    #If element to the right is greater, values are sorted in increasing order, i increments, and loop checks next pair, lst[i] and lst[i+1].
    #if element to the right is less than element at i, list is not sorted in increasing order
    
    for i in range(len(lst)-1):             #1st i = O(1). Loop runs N-1 times
        if int(lst[i])<= int(lst[i+1]):     # worst case 2 operations for each loop = (N-1)*(1+1)
            i += 1                          # last check of i = O(1)
        else:
            return False
    return True                             #O(1) for return
                                            #for loop total: O(1) + O(1) + O(1) + O(N-1)(1+1) = O(3) + O(2N) = O(N)


#Asks for file name and calls is_file_sorted function
#Outputs respective user-friendly message

filename = input("Please enter file name: ")    #O(1)
if is_file_sorted(filename) == True:            #O(1)
    print('Congratulations! The file', filename, 'is nicely sorted!')       #O(1)
    
else:
    print('Looks like the file', filename, 'needs to be sorted')        #O(1)


#Total big-Oh running time: is O(N). Adding up constant time operations with the read function and for loop total times:
    #O(1) + O(N) + O(1) + O(N) + O(1) +O(1) + O(1) + O(1) =
    #O(N) + O(N) + O(6) =
    #O(N) + O(N) =
    #2N =
    #O(N)

    
