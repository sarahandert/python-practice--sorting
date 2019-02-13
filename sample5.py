
"""Name: Sarah Andert
    Course: CMPS 1500
    Date: 10/29/2018
    Analysis of runtime for sort programs (merge sort and selection sort) that use a list of randomly generated numbers as input from a file,
    sort them in ascending order, and write the sorted list to the output file.

>>>>>Enter the filename: test.py
Enter number of values: 7
Please enter output file name: result.py
It took 0.000225 seconds to input values from file test.py
It took 6.1e-05 seconds to sort 7 values using merge sort
It took 0.000449 seconds to output 7 sorted values to file result.py
Total time the program took is 0.000735 seconds

It took 0.000207 seconds to input values from file test.py
It took 3.4e-05 seconds to sort 7 values using selection sort
It took 0.000485 seconds to output 7 sorted values to file result.py
Total time the program took is 0.000726 seconds


>>>>>Enter the filename: test.py
Enter number of values: 3
Please enter output file name: result.py
It took 0.000218 seconds to input values from file test.py
It took 3.2e-05 seconds to sort 3 values using merge sort
It took 0.000389 seconds to output 3 sorted values to file result.py
Total time the program took is 0.000638 seconds

It took 0.000208 seconds to input values from file test.py
It took 2.3e-05 seconds to sort 3 values using selection sort
It took 0.000206 seconds to output 3 sorted values to file result.py
Total time the program took is 0.000437 seconds

"""

#import modules for generate_nums function and for analyze_merge and analyze_selection functions
import random
import time

# Function to generate random list of numbers (length of list input by user) and write to a file
def generate_nums(filename, n):
    """ int->str
        >>>generate_nums(test.py, 3)
        [3\n, 7\n, 21\n]
        >>>generate_nums(test.py, 7)
        ['3\n', '7\n', '21\n', '14\n', '100\n', '29\n', '37\n']
    """

    random.seed(0)
    f = open(filename, 'w')
    counter = 0
    while counter < n:     # counter tracks the total number of values requested by user input, n, in main program
        f.write(str(random.randrange(0,100)) + "\n")      #writes each value generated to a new line in the file
        counter += 1
    f.close()
    
#Merge sort function definitions__________________________________________________________

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

#Selection sort function definitions________________________________________________________________

def selection_sort( aList ):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len( aList )
  for i in range( n - 1 ):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range( i + 1, n ):
      if aList[ j ] < aList[ smallNdx ] :
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[ i ]
    aList[ i ] = aList[ smallNdx ]
    aList[ smallNdx ] = tmp

  return aList

#Analysis of mergesort runtime__________________________________________________________________


def analyze_mergesort(inputfile, outputfile):

    t = time.time() 
    
    f = open(inputfile, 'r') 
    lst = f.readlines()
    f.close()


    t1 = time.time()
    time_difference1 = t1 - t 
    print("It took", round(time_difference1, 6), "seconds to input values from file", inputfile) 

    t = time.time() 
    for i in range(len(lst)):       #converts list of strings stored in file to integers
        lst[i] = int(lst[i])

    sorted_lst = merge_sort(lst)
    
    t1 = time.time()
    time_difference2 = t1 - t 
    print("It took", round(time_difference2, 6), "seconds to sort", n, "values using merge sort")

    t = time.time()
    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])   #converts integers that were sorted back into strings to write to file
        f.write(sorted_lst[i] + "\n")
    f.close()

    t1 = time.time()
    time_difference3 = t1 - t 
    print("It took", round(time_difference3, 6), "seconds to output", n, "sorted values to file", outputfile)
    print("Total time the program took is", round((time_difference1 + time_difference2 + time_difference3), 6), "seconds")
    print()
    
#Analysis of selection sort runtime_____________________________________________________________
    
def analyze_selection(inputfile, outputfile):
    
    t = time.time() 
    f = open(inputfile, 'r') 
    lst = f.readlines()
    f.close()

    t1 = time.time()
    time_difference1 = t1 - t 
    print("It took", round(time_difference1, 6), "seconds to input values from file", inputfile) 

    t = time.time() 
    for i in range(len(lst)):
        lst[i] = int(lst[i])

    sorted_lst = selection_sort(lst)

    t1 = time.time()
    time_difference2 = t1 - t 
    print("It took", round(time_difference2, 6), "seconds to sort", n, "values using selection sort")
    
    t = time.time()
    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])
        f.write(sorted_lst[i] + "\n")
    f.close()

    t1 = time.time()
    time_difference3 = t1 - t 
    print("It took", round(time_difference3, 6), "seconds to output", n, "sorted values to file", outputfile)
    print("Total time the program took is", round((time_difference1 + time_difference2 + time_difference3), 6), "seconds")

#main program__________________________________________________

# calls generate_nums function to generate list of n random numbers to be stored in filename
filename = input('Enter the filename: ')
n = int(input('Enter number of values: '))

generate_nums(filename, n)

#uses filename with stored random values as input to analyze_mergesort and analyze_selection functions. Saves sorted list to output file
inputfile = filename
outputfile = input('Please enter output file name: ')

analyze_mergesort(inputfile, outputfile)
analyze_selection(inputfile, outputfile)


