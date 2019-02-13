"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Section: Tuesday, CMPS 1501-05 11-12.15 pm
    Assignment: lab6pr1.py
    Date: 10/29/2018
    Program to take input from a file containing a list of numbers, one number per line, sort them using mergsort function, and output
    sorted numbers to output file, one number per line

    """
def merge( left, right ):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    # Repeatedly move the smallest of left and right to the new list
    while lt < len( left ) and rt < len( right ):
        if left[ lt ] < right[ rt ]:
            aList.append( left[ lt ]  )
            lt += 1
        else:
            aList.append( right[ rt ] )
            rt += 1

    # There will only be elements left in one of the original two lists.

    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append( left[ lt ] )
        lt += 1
         
    # Append the remains of right (rt..end) on to the new list.
    while rt < len( right ):
        aList.append( right[ rt ] )
        rt += 1

    return aList

def merge_sort( aList ):
    """
    Merge sort recursively divide the list into half, sort both halves
    and then merge the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len( aList ) <= 1:
        return aList

    else:
        mid = len( aList ) // 2

        # Recursively sort the left and right halves
        left = merge_sort( aList[ :mid ] )
        right = merge_sort( aList[mid:] )
        
        # Merge the two (each sorted) parts back together
        return merge( left, right )


    
def use_mergesort(inputfile, outputfile):
    f = open(inputfile, 'r') 
    lst = f.readlines()
    f.close()

    for i in range(len(lst)):
        lst[i] = int(lst[i])

    sorted_lst = merge_sort(lst)

    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])
        f.write(sorted_lst[i] + "\n")
    f.close()

#main program
inputfile = input('Please enter input file name: ')
outputfile = input('Please enter output file name: ')

use_mergesort(inputfile, outputfile)
    

