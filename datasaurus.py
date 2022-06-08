
#python program to read a csv file and scatterplot the data based on the dataset group

import csv
from decimal import Decimal
import matplotlib.pyplot as plt

# creating empty list to store values later
x_coordinates = []
y_coordintes = []
different_items = []
whole_data = []

#for count
i = 0
j = 1

#reading the csv file
with open("data1.tsv") as file: 
    tsv_file = csv.reader(file, delimiter="\t")
    next(tsv_file)
    for each_list in tsv_file:
        whole_data.append(each_list) #reading a csv file to another data for later use
    file.close()

#storing only unique data set name for iteration and comparision
for indv_list in whole_data:
    if indv_list[0] not in different_items: 
        different_items.append(indv_list[0])

#looping on each unqiue data set
for items in different_items:

        x_coordinates.clear() #for new coordinates of each data set
        y_coordintes.clear()

        for each_data in whole_data:
            if each_data[0] == items: #comparing the dataset name to the each dataset name stored in different_items
                
                x_coordinates.append(Decimal(each_data[1]))
                y_coordintes.append(Decimal(each_data[2]))

                name = each_data[0] #storing name for the scatterplot title
        
        i += 1 
        j += 1
        
        #number of figures to be presented
        plt.figure(i)

        #function to plot the data based on the given imputs
        plt.scatter(x_coordinates, y_coordintes, color= "green",
                    marker= "*", s=50)

        # plot title
        plt.title(name)

        plt.xlabel('x-axis')
        plt.ylabel('y-axis')

        # function to show the plot
        plt.show()
