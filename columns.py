
import csv
import re
from io import StringIO
import pandas as pd

###########para ordenar un txt################
#output_file = open("output3.csv", "w")
#with open('prueba.txt', 'r') as r:
 #   for line in sorted(r):
  #      output_file.write(line)
        

#########eliminar numero repetidos#######

#lines_seen = set()  # holds lines already seen
#outfile = open('output_final.csv', "w")
#infile = open('output3.csv', "r")
#print ("The file bar.txt is as follows")
#for line in infile:
 #   if line not in lines_seen:  # not a duplicate
 #       outfile.write(line)
 #       lines_seen.add(line)
#outfile.close()

#####leer un csv#######

#with open('text.txt') as f_in:
 #   with open('output.csv', 'w') as f_out:
#
 #       for line in f_in:
  #          city = line.rstrip('\n')
   #         f_out.write(city)
           
        

#max_number= 10
#number = 0
list_number = ""
acum = 999000000
filename = "output.csv"



for min_number in range (500):
  for i in range (2000):
    number = "51"+ str(acum)+","
    list_number= list_number + number
    acum = acum+1
  list_number = list_number + "\n"
#print (list_number)

with open("salidas.csv", "w") as text_file:
    text_file.write(list_number)




#with open(filename, 'w') as csvfile:
 # for row in reader:
  #  csvwriter = csv.writer(csvfile)    
   # csvwriter.writerows(row) 


