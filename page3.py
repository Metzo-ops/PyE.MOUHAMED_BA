from posixpath import split
import don_inv
import csv
import date
import moyenne
liste = []
liste_note = []
with open("donnees.csv", encoding='utf8') as File:
    reader = csv.reader(File)
    don_inv.func_inv(reader)
    date.dat(reader) 
    for i in reader:
        liste.append(i)
        liste_note = liste[6].split("#") 
        claire = liste_note.split("[")
        liste_note1 = claire[1].split(":")
        liste_dev = liste_note1[0].split(";")
        moyenne.moy(liste_dev)
