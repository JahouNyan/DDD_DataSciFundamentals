#Welcome to myprogram
firstname = input ("Welcome to my programme, what is your name? ")
print(firstname + ", welcome to my programme! Let's get to know each other better. ")
surname = input ("What is your last name? ")

#Check for family relations
surname = surname.capitalize().strip()
if surname == "Mensah":
    print("Hey, you should feel right at home here.")
else:
    print ("Hi, " + surname)
    
#input you birthyear and check for age limit
age = input("What year were you born? ")
age = int(age)
agelimit = (2018 - age)
if agelimit >= 18:
    print ("Let's get started. ")
else:
    print ("Sorry, you are too young. Goodbye.")
    
#Calculate user value to advertiser
#age datapoint
if (agelimit >= 18) + (agelimit <= 45):
    agelimitvalue = 10
else:
    agelimitvalue = 1
    
#name datapoint
namelength = len(firstname)
namelength = int(namelength)
if (namelength <= 7 ):
    namevalue = 10
else:
    namevalue = 5

#surname datapoint
if surname == "MENSAH":
    surnamevalue = 10
else:
    surnamevalue = 5

#calculate advalue
advalue = (agelimitvalue + namevalue + surnamevalue)
if advalue >= 30:
    print ("*Great catch")
else:
    print ("***More work to be done.")
    
#additional info and feedback
sex = input ("Are you male or female? ")
sex = sex.lower().strip()
if (sex == "male"):
    print ("Mr. " + surname + " we have one final question...")
elif (sex == "female"):
    print ("Ms. " + surname + " we have one final question...")
else:
    print ("Input error")
    
occupation = input ("What do you do? Student, Worker or Other. Please select one. ")
occupation = occupation.lower().strip()
if (occupation == "student"):
    print ("Your school work just got easier!")
elif (occupation == "worker"):
    print ("Networking at your finger tips!")
elif occupation == "other":
    other = input("tell us more: ")
else:
    print ("I do not understand your input.")
    
#goodbye statement
print ("See you later!")
quit()


    
