# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:12:16 2022

@author: Dave
"""


'''MEDIA & SOCIETY Analytical Work
link = https://docs.google.com/document/d/1tOvQ9csCMm3Mit91cB9aaS-5d53rnVWTAeobpqi4aoI/edit

Using numpy, pandas and matplotlib to create a simple bar plot
showing average usage of 6 different social media services 

--------------------------------------------------------------
-SNAPCHAT
-INSTAGRAM
-YOUTUBE
-FACEBOOK
-iMESSAGE
-NETFLIX

1. Create Average amount of time per day
2. Total screen time per day (Subjective to the apps I selected)
3. Perhaps 3 different graphs representing 
'''



import numpy as np
import matplotlib.pyplot as plt
import csv

def plot(keys,values,color,day):
    pColor = str(color).lower()
    figure = plt.figure(figsize=(8,3))
    
    plt.bar(keys,values,color=pColor,width=0.3)
    plt.xlabel("MEDIA TYPES")
    plt.ylabel("# OF HOURS")
    plt.title(day)
    plt.show()

'''1'''
file = open("MEDIAspreadsheet.csv")
csvreader = csv.reader(file)


header = []
header = next(csvreader)
header.remove(header[0])

rows = []
for row in csvreader: 
    rows.append(row)



#creating copied list; copy function was aliasing for some reason

newRows = []
for g in range(len(rows)):
    newRows.append([])
    for h in range(len(rows[g])):
        newRows[g].append(rows[g][h])
        
        
   
#Shows the frequency of each app per day
dictionary = dict()
for i in range(len(rows)):
    dictionary[rows[i][0]] = {"SNAPCHAT": float(rows[i][1]), "INSTAGRAM":float(rows[i][2]), "YOUTUBE":float(rows[i][3]), \
                              "FACEBOOK":float(rows[i][4]), "iMESSAGE":float(rows[i][5]), "ONLINE ARTICLES":float(rows[i][6])}


#regular dictionary to plot
dictionary2 = dict()
weekdayL = []
    
for j in range(len(newRows)):
    weekdayL.append(newRows[j][0])
    del newRows[j][0]
   

for names in header: 
    dictionary2[names] = 0
    

    
for k in range(len(newRows)):
    for items in dictionary2:
        if items == "SNAPCHAT":
            dictionary2[items] +=( float(newRows[k][0]) )
        elif items == "INSTAGRAM":
            dictionary2[items] += ( float(newRows[k][1]) )
        elif items == "YOUTUBE":
            dictionary2[items] += ( float(newRows[k][2]) )
        elif items == "FACEBOOK":
            dictionary2[items] += ( float(newRows[k][3]) )
        elif items == "iMESSAGE":
            dictionary2[items] += ( float(newRows[k][4]) )
        elif items == "ONLINE ARTICLES":
            dictionary2[items] += ( float(newRows[k][5]) )
     


for items in dictionary2:
    dictionary2[items] /= 3
    dictionary2[items] = round(dictionary2[items],4)
        

#plot
apps = list(dictionary2.keys())
values = list(dictionary2.values())

print("#1")

figure = plt.figure(figsize=(10,5))

plt.bar(apps,values,color="blue",width=0.4)
plt.xlabel("MEDIA TYPES")
plt.ylabel("# OF HOURS")
plt.title("SOCIAL MEDIA USAGE OVER PAST 3 DAYS (#1)")
plt.show()


print("-------------------------------------------------------------")

'''2'''
print("#2")


countL = []
ct1, ct2, ct3 = 0, 0, 0
newLists = [[float(newRows[y][x]) for x in range(len(newRows[y]))] for y in range(len(newRows))]

for num in range(len(newLists)):
    if num == 0:
        ct1 += round(sum(newLists[0]),5)
    elif num == 1:
        ct2 += round(sum(newLists[1]),5)
    elif num == 2:
        ct3 += round(sum(newLists[2]),5)
    
countL.append(ct1)
countL.append(ct2)
countL.append(ct3)


figure2 = plt.figure(figsize=(10,5))

plt.bar(weekdayL, countL, color = "red", width = 0.4)
plt.xlabel("DAYS")
plt.ylabel("HOURS")
plt.title("TOTAL PHONE USAGE (#2)")
plt.show()


print("-------------------------------------------------------------")
'''3'''
print("#3",end="\n\n")
print("Sunday")
SUNDAY = dictionary["SUNDAY"]
sunKey = list(SUNDAY.keys())
sunVal = list(SUNDAY.values())

plot1 = plot(sunKey,sunVal,"cyan","SUNDAY")

print()
print("Monday")
MONDAY = dictionary["MONDAY"]
monKey = list(MONDAY.keys())
monVal = list(MONDAY.values())

plot2 = plot(monKey,monVal,"green","MONDAY")

print()
print("Tuesday")
TUESDAY = dictionary["TUESDAY"]
tueKey = list(TUESDAY.keys())
tueVal = list(TUESDAY.values())

plot3 = plot(tueKey,tueVal,"orange","TUESDAY")
