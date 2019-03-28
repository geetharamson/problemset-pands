# Geetha Karthikesan, 2019
#sumupto a given number 
# input a positive integer  
i= int(input("please enter a positive integer:"))
# entering value of sum as 0

sum = 0
#checking whether i is greater than 0
while i >0:
  #value of  sum becomes sum +i
  sum = sum + i
  # new value of i becomes i-1
  i = i-1
# print sum 
print (sum)
