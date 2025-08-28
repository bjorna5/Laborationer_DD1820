from class_drama import Drama

import csv

def read_file_to_list(filnamn):
    with open(filnamn, mode="r") as dramafil:
        list = []
        csvfile = csv.reader(dramafil, delimiter=",")
        next(csvfile)

        objekt1 = Drama(next(csvfile))
        objekt2 = Drama(next(csvfile))

        return objekt1, objekt2
    

def main():

    (drama1, drama2) = read_file_to_list("kdrama.txt")

    # Kollar __init__ metoden (urval)
    print(drama1.name)
    print(drama2.rating)
    print(drama1.year)
    print(drama2.actors)
    print("\n")

    # Kollar __str__ metoden
    print(drama1)
    print(drama2)
    print("\n")

    # Kollar __lt__ metoden
    if drama1 < drama2:
        print (drama1, "har lägre rating än", drama2)
    else:
        print (drama2, "har lägre rating än", drama1)
    print("\n")

    # Kollar no_of_writers metoden
    print(drama1.no_of_actors())
    print(drama2.no_of_actors())
    print("\n")

    # Kollar before_2015 metoden
    print(drama1.before_2015())
    print(drama2.before_2015())


main()
