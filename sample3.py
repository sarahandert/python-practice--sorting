
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



def use_selection(inputfile, outputfile):
    f = open(inputfile, 'r') 
    lst = f.readlines()
    f.close()

    for i in range(len(lst)):
        lst[i] = int(lst[i])

    sorted_lst = selection_sort(lst)

    f = open(outputfile, 'w')
    for i in range(len(sorted_lst)):
        sorted_lst[i] = str(sorted_lst[i])
        f.write(sorted_lst[i] + "\n")
    f.close()



#main program
inputfile = input('Please enter input file name: ')
outputfile = input('Please enter output file name: ')

use_selection(inputfile, outputfile)
