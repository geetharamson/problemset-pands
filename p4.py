# Geetha Karthikesan , 2019
# python collatz .py

# calling function def collatz
def collatz(num):
    # to check whether the num is fully divisible by 2 with remainder 0
    if num % 2 == 0:
        # then divide the num by 2
        return num // 2
        # else if num when divided by 2  has remainder of 1
    elif num % 2 == 1:
        # return num*3 + 1
        return 3 * num + 1

   # inputing a positive no for the integer
integer = int(input('Enter a positive integer: '))
  # print the integer
print (integer)

 # while the integer value isnot equal to 1
while integer != 1:
    # integer gets the collatz value of integer
    integer = collatz(integer)
    # print integer
    print (integer)

# Reference
# python tutorial
# Adapted from https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
