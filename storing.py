# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:00:46 2018

@author: Jahou
"""
#Print the contents of the list, formatted with index number
newfile = open("politicians2.csv", "a")
csv = open("politicians.csv")

for index, line in enumerate(csv):
    line = line.strip().split(",")
    firstname = line [0]
    lastname = line[1]
    birthyear = line[2]
    party = line[3]
    politiciansindex = str(index)
    newline = (politiciansindex + ": " + firstname +" "+ lastname +" was born in " + birthyear + " and is member of " + party +" party.")
    newfile.write(newline)
    newfile.write("\n")


#convert csv file to list and then save
#remember to convert it back
csv.close()
#Ask for four options: remove a person, add a person, save the database to csv or quit the program.

newline = input("What do you want to do: add or remove a person? ")
newindex = [index+1]
if newline =="add":
    newfirstname = input("What is the first name of the politician? ")
    newlastname = input("what is the last name of the politician?: ")
    newbirthyear = input("What year was he/she born? ")
    newparty = input("What party do they belong to? ")
    newindex.append(index)
    newindex = str(index)
    newentry = (newindex + ": " + newfirstname +" "+ newlastname +" was born in " + newbirthyear + " and is member of " + newparty +" party.")

# =============================================================================
# elif newline == "remove":
#     removeperson = input("What is the name of the person you want to remove?: ")
#         if remove name == 
#     #removelist = input("Please provide index numbers you want to remove: ")
# newfile.write(newentry)
# newfile.write("\n")
# 
# =============================================================================
    

newfile.close()

        