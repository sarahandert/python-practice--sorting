



def generate_nums(filename, n):
    import random
    random.seed(0)
    f = open(filename, 'w')
    counter = 0
    while counter < n:
        f.write(str(random.randrange(0,100)) + "\n")
        counter += 1
    f.close()


filename = input('Enter the filename: ')
n = int(input('Enter the length of number list: '))

generate_nums(filename, n)
