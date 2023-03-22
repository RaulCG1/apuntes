#Manejo de ficheros

txt_file=open("Basico++\my_file.txt","w+") #r+ leer y escribir
txt_file.write("Mi nombre es raul\nMi apellido es Calderon\nTengo 23 years")

#print(txt_file.read(10))

#print(txt_file.readline())

for line in txt_file.readlines():
    print("1")
    print(line)

#print(txt_file.readlines())

txt_file.write("\nHola")


txt_file.close()
import os

os.remove("Basico++\my_file.txt")


#json 

import json

json_file= open("Basico++\my_file.json","w+")
json_text= {"Nombre":"Raul",
            "Apellido":"Calderon",
            "Edad":23,
            "Lenguajes": ("Pyton","Java","C","C#")}

json.dump(json_text,json_file,indent=4)

json_file.close()

json_file= open("Basico++\my_file.json","r")

for linea in json_file.readlines():
    print(linea)


json_dic=json.load(open("Basico++\my_file.json"))

print (json_dic)

#csv files
import csv
cvs_file= open("Basico++\my_file.csv","w+")

csv_writer = csv.writer(cvs_file)
csv_writer.writerow(["Nombre","Apellido","Edad","Lenguaje"])
csv_writer.writerow(["Raul","Calderon",23,"Python"])
csv_writer.writerow(["Paco","Garcia",31,"C"])
cvs_file.close()

cvs_file= open("Basico++\my_file.csv","r")

#for valor in cvs_file.readlines():
 #   print(valor)
cvs_leer =csv.DictReader(cvs_file,dialect=1)
for fila in cvs_leer:
    print(type(fila))
#.xlsx files
# import xlrd debe instarlse 
#.xml files
import xml

