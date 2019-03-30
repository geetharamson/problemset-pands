# Geetha Karthikesan ,2019
# divisors.py
#program to output nos between 1000 & 10000 divisible by 6 not 12

# Using for loop to set n is the no ranging from 1000 to 10000
for  n in range (1000, 10000):
  # modulus operator will evaluate 0 only when no is divisible 
    if n % 6 ==0  and  n % 12 != 0 :
    # print n
      
     print (n) 
     # increment the value of n by 1  
    n=n+1


