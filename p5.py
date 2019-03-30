# Geetha Karthikesan ,2019
#python primes.py 
# num is any positive integer u need to check its prime or not
num = int (input("Please enter a positive integer:"))

# prime numbers are greater than 1
if num > 1:
   # check for factors in the range (2,num)
   for i in range(2,num):
    # checking if num is completely divisible by i 
       if (num % i) == 0:
     # print it isnt a prime number    
           print("This is not a prime number")
      # Break the loop
           break
      # else then   
   else:
      # print its a prime number
       print("That is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print("That is not a prime number")
   
   
   # References
   # pythontutorial
   # https://stackoverflow.com
   # python crash course book
