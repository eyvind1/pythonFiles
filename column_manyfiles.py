import csv
import winsound

my_file = open("archivos\\Libro2.txt","r")
#output_file = "output\\file_usuariosfacebook.csv"  
content = my_file.read()
content_list = content.split("\n")
total_filas = len(content_list)
bloques = 100
total = total_filas/bloques
acum = 0
list_text = ""
#text = ""


for i in range (total):
    #output_file = "output\\archivos\\prueba"+str(i)+".txt"
    f = open("output\\archivos\\prueba"+str(i)+".txt","w")
    for j in range (bloques):
        text = content_list[acum]  
        list_text = list_text + text+'\n'
        acum = acum+1
        #print text
    #with open(output_file, "w") as text_file:
    f.write(list_text)
    f.write("\n")
    list_text = "" 

#print list_text


winsound.MessageBeep()