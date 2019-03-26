#Geetha Karthikesan , 2019
#python secondstring.py


# Initialising a string sentence
sentence = input ("Enter a sentence :")

# Printing Entered Sequence
print ("Entered sequence : " + sentence)

# To split  each words in the sentence.
words = sentence.split()

# After spliting each words just printing out the words 
print (words)

# Using range function to choose alternate words
for i in range (0,len(words), 2):

    # prints out the alternate words from the list
    print (words[i] )


   # References  - Python 3.6 Tutorial
    #             - Python Crash Course 
    # https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
