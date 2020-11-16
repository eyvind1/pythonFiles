import csv
import math

my_file = open("archivos\\usuariosfacebook.txt","r")
output_file = "output\\file_usuariosfacebook.csv"

list_text =""
columnas = 5000
content = my_file.read()
content_list = content.split("\n")
#print(content_list.)
#my_file.close()
total = len(content_list)
acum = 0
#filas = total/columnas

if total%columnas == 0:
    filas = total/columnas
else:
    filas = (total/columnas)+1

print filas
#for min_number in range (columnas):
 # for i in range (filas):
  #  if acum < total:
   #     text = content_list[acum] + ","
    #    list_text= list_text + text
     #   acum = acum + 1
    #else:
     #   list_text = list_text + ","
  #list_text = list_text + "\n"

#with open(output_file, "w") as text_file:
 #   text_file.write(list_text)
#print (list_text)