import csv
import winsound

acum = 0
nro_columnas = 2000


for i in range (nro_columnas):
    f = open("C:\\Users\\51921\\Desktop\\output\\9990-9999\\salida"+str(i)+".txt","w")
    with open("salidas.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for lines in csv_reader:
            #print(lines[i])
            f.write(lines[i])
            f.write("\n")
winsound.MessageBeep()





      