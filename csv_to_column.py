import csv
import winsound

acum = 0
nro_columnas = 47
#path = "C:\\Users\\51921\\Desktop"
#file_name = "instagram_545356" 
#extension = ".csv"

for i in range (nro_columnas):
    f = open("C:\\Users\\51921\\Desktop\\instagrampatoparodi\\file_instagrampatoparodi"+str(i)+".txt","w")
    #f=open(path+file_name+extension,"w")
    with open("output\\file_instagrampatoparodi.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for lines in csv_reader:
            #print(lines[i])
            f.write(lines[i])
            f.write("\n")
winsound.MessageBeep()





      