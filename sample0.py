"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Section: Tuesday, CMPS 1501-05 11-12.15 pm
    Date: 10/29/2018
    Program to take input from a list of numbers or a file containing a list of numbers and check if they are in
    increasing order

(str)-> int->Bool
>>>>[4, 5, 6, 7, 8]
True
>>>>[4, 3, 29, 0, 7]
False
>>>>[-12 0 21 100]
True
>>>>[25 -75 1 2 3]
False

"""

# function definitions
def is_sorted(lst):
    if len(lst) == 1:
        return True
    for i in range(len(lst)-1):
        if lst[i]<= lst[i+1]:
            i += 1
        else:
            return False
    return True

def is_file_sorted(filename):
    f = open(filename, 'r')
    lst = f.readlines()
    f.close()
    print(lst)
    
    for i in range(len(lst)-1):
        if int(lst[i])<= int(lst[i+1]):
            i += 1
        else:
            return False
    return True
    
    
# gets input from keyboard, converts string to integer list, and calls is_sorted function
user_input = input('Enter a list of numbers separated by spaces: ')
result = ''
for ch in user_input:
    if ch != ',':
       result = result + ch
    else:
        result = result + ' '
    
nums = result.split()
lst =[]
for num in nums:
    lst.append(int(num))
    


print(is_sorted(lst))

# calls is_file_sorted function using test.py as input
print(is_file_sorted("test.py"))






     
    
