import csv
import winsound

my_file = open("archivos\\32.txt","r")
#output_file = "output\\file_usuariosfacebook.csv"  
content = my_file.read()
content_list = content.split("\n")
total_filas = len(content_list)
bloques = 40
#total = total_filas/bloques
acum = 0
list_text = ""
#text = ""

if total_filas%bloques == 0:
    total = total_filas/bloques
else:
    total = (total_filas/bloques)+1

for i in range (total):
    #output_file = "output\\archivos\\prueba"+str(i)+".txt"
    f = open("output\\archivos\\wpp"+str(i)+".txt","w")
    for j in range (bloques):
        if acum < total_filas:
            text = content_list[acum]  
            list_text = list_text + text+'\n'
            acum = acum+1
        else :
            list_text = list_text +'\n'
        #print text
    #with open(output_file, "w") as text_file:
    f.write(list_text)
    f.write("\n")
    list_text = "" 

#print list_text


winsound.MessageBeep()