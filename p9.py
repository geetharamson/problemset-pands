# Geetha Karthikesan , 2019
# p9.py moby-txt
# Import sys
import sys 

# Input value of fileName as sys.argv[1]
fileName =sys.argv[1]

#print fileName 
print (fileName)

# Opening  fileName and reading 
fileObject = open (fileName, 'r')

#Initialising index as 1
index = 1

# Using for loop to print alternate lines 
for line in fileObject :
    index = index + 1
    
    if index % 2 == 0:
     # print line and omit the blank space      
      print(line.rstrip())

# Closes the fileObject
fileObject.close()

# Reference
  #Python Tutorial
   # geeksforgeeks.org 
   # python crash course
