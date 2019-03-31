# Geetha Karthikesan ,2019
#program to display a plot function  x ,square of x and 2power x in range (0,4)

# importing matplotlib 
import matplotlib.pyplot as plt
# inputing the values of x axis for the plot
input_values = [0,1,2,3,4]
# squares of the inpt values
squares = [0,1,4,9,16]
# have to plot 2power of input values
exp =[1,2,4,8,16]

#plot graph with the input values,squares,exp in x-axis against linewidth of 5 in y-axis
plt.plot(input_values,squares,exp ,linewidth = 5)
# shows the graph
plt.show() 



---Sorry Ian something is wrong with Matplotlib in my laptop and I dont know to fix it yet, so cant check whether is this write ! 
# Reference
# python crash course
