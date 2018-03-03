import csv
import numpy as np
import numpy as genfromtxt
import matplotlib.pyplot as plt
from collections import Counter
'''Import from csv file'''
def readData():
	with open('data.csv', 'r') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)

	your_list.pop(0)
	return your_list


'''plot data'''
def plotData(your_list, unknown_fruit):
	weight   = [ i[0] for i in your_list]
	color  = [ i[1] for i in your_list]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	plt.xlabel('Color (3 Banana | 1,4 Apple)')
	plt.ylabel('Weight')
	plt.title('Friuts')
	ax.scatter(color ,weight, c='b', marker="s", label='Training Data')
	ax.scatter(unknown_fruit[0] ,unknown_fruit[1], c='r', marker="s", label='Test Data')
	plt.legend(loc='upper left')
	plt.show()


'''Distance count between two point(fruits)'''
def distance(fruit1, fruit2):
	    # first let's get the distance of each parametertem
    a = int(fruit1[0]) - fruit2[0]
    b = int(fruit1[1]) - fruit2[1]
    
    # the distance from point A (fruit1) to point B (fruit2)
    # a^2 + b^2 = c^2
    c = (a**2 + b**2) **0.5
    return c


def main():
	your_list = readData()
	# the unknown fruit from above
	unknown_fruit = [1, 302]

	# This is arbitrarily chosen for this example. Generally
	# you need to play with this magic number to find what works
	# best for your case.
	k = 3

	# using the distance() function from above, sort
	# the data set by smallest distances on top
	sorted_dataset = sorted(your_list, key=lambda fruit: distance(fruit, unknown_fruit))
	top_k = sorted_dataset[:k]
	
	class_counts = Counter(fruit for (weight, color, fruit) in top_k)
	
	# class_counts now looks like this:
	# {"apple": 3}
   
	# get the class with the most votes
	classification = max(class_counts, key=lambda cls: class_counts[cls])
	print classification
	plotData(your_list, unknown_fruit)

main()