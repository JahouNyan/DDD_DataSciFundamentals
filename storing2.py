

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:00:46 2018

@author: Jahou
"""
#Read the provided csv file and convert the data to a multidimensional list (list with lists)
csv = open("politicians.csv")


#lines = list(csv)
for index, line in enumerate(csv):
    for line in csv:
        line = line.strip().split(",")
        firstname = line[0]
        lastname = line[1]
        birthyear = line[2]
        party = line[3]
        polindex = str(index)


#Print the contents of the list properly formatted with the index number and number of entries
        newline = (polindex + ": " + firstname +" "+ lastname +" was born in " + birthyear + " and is member of " + party +" party." + "\n")
        entrynum = len(list(csv))
        print(newline)
        print("This file contains " + str(entrynum) + " records.")
    
csv.close()
csv = open("politicians.csv")

#Ask for four options: remove, add, save to csv or quit.
        
for newentry in csv:
    newentry = input("Do you want to: add, remove, save or quit database? ")
    while newentry =="add":
            newfirstname = input("What is the first name of the politician? ")
            newlastname = input("what is the last name of the politician?: ")
            newbirthyear = input("What year was he/she born? ")
            newparty = input("What party do they belong to? ")
            newindex = str(index)
            newline = (polindex + ": " + newfirstname +" "+ newlastname +" was born in " + newbirthyear + " and is member of " + newparty +" party." + "\n")
            print (newline)
            newentry = (newfirstname + "," + newlastname +  "," + newbirthyear +  "," + newparty)
    csv = open("politicians.csv", "a")
    csv.write(newentry)
    csv.write("\n")
    csv.close()
    if newentry == "remove":
              removeindex = input("Index number of the person to be removed: ")
              removeindex=int(removeindex)
              del csv[removeindex]
                      
    elif newentry == "quit":
        csv.close()
    else:
        quit(csv)
        csv.close()




#‘Remove a person’ should ask for an index number, and then remove that person from the list.
#‘Add a person’ should ask for the same four fields that also exist in the original CSV file and add those to the list.
#‘Save the database’ should save the modified list in the same format in the original file so that whenever the program is quit and run again the mutations done in the program are properly reflected in the file. Alternatively, the list should be saved whenever the user 'removes' or 'adds' a person.
#The program should indefinitely provide the four options again after an action is completed until the use chooses the 'quit the program' option.
         
