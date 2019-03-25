# Geetha Karthikesan ,2019
#program to print x ,square of x and 2 exponent x in range (0,4)

for x in range (0,4):
    # to find square of no in the range 
 squares =(x ** 2 for x in range (0,4)) 

 # to find 2 power of a no 
 power = pow (2,x)
print ( x, squares , power ) 

