
#python primes.py 
# num is any positive integer u need to check its prime or not
num = int (input("Please enter a positive integer:"))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("This is not a prime number")
           break
   else:
       print("That is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print("That is not a prime number")