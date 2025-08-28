from class_drama import Drama

import csv

def read_file_to_list(filnamn):
    with open(filnamn, mode="r") as dramafil:
        list = []
        csvfile = csv.reader(dramafil, delimiter=",")
        next(csvfile)
        
        for line in csvfile:
            if len(line) == 10:
                objekt = Drama(line)
                list.append(objekt)
    return list

def search(lista):
    while True:
        eftersokt_drama = input("Sök efter ditt favoritdrama i vår katalog: ")
        found = False
        for drama in lista:
            if drama.name.lower() == eftersokt_drama.lower():
                found = True
                found_drama = drama.name

        if found == True:
            print("Vi har ", found_drama, " i vår katalog!")
            break
        else:
            print("Det verkar inte som att vi har", eftersokt_drama, "i vår katalog. Försök igen!")




dramalist = read_file_to_list("kdrama.txt")
search(dramalist)

