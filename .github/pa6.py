#Programmers: Callie Walker, Lesdy Galvez
#Course: CS151 Dr. Rajeev
#Date: 12/4/21
#Programming Inputs: Data from the storm1 file, number for crop damage, type of storm
#Programming Outputs: Average days a type of storm occurred, difference in direct deaths and injuries, the amount of storms with (at least) that amount of damage, bar graph showing property damage
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
Start_Year_And_Month = 0
Start_Day_Of_Month = 1
Start_time = 2
End_Year_and_Month = 3
End_Day_of_Month = 4
End_time = 5
Storm_name = 6
Storm_Type = 7
num_of_injuries_directly = 8
num_of_injuries_indirectly = 9
num_of_deaths_directly = 10
num_of_deaths_indirectly = 11
amount_of_damage_property = 12
amount_of_damage_crops = 13
#This file opens and reads a file to store its contents in a list.
def readfile(filename):
    data = []
    try:
        f = open(filename, "r")
        line_count= 0
        for line in f:
            try:
                line_count += 1
                line_entries = line.split(",")
                line_entries[Start_Year_And_Month] = (line_entries[Start_Year_And_Month])
                line_entries[Start_Day_Of_Month] =(line_entries[Start_Day_Of_Month])
                line_entries[Start_time]=(line_entries[Start_time])
                line_entries[End_Year_and_Month]=(line_entries[End_Year_and_Month])
                line_entries[End_Day_of_Month]=(line_entries[End_Day_of_Month])
                line_entries[End_time]=(line_entries[End_time])
                line_entries[Storm_name] = line_entries[Storm_name].strip()
                line_entries[Storm_Type] = line_entries[Storm_Type].strip()
                line_entries[num_of_injuries_directly] = (line_entries[num_of_injuries_directly])
                line_entries[num_of_injuries_indirectly] = (line_entries[num_of_injuries_indirectly])
                line_entries[num_of_deaths_directly] = (line_entries[num_of_deaths_directly])
                line_entries[num_of_deaths_indirectly]=(line_entries[num_of_deaths_indirectly])
                line_entries[amount_of_damage_property] = (line_entries[amount_of_damage_property])
                line_entries[amount_of_damage_crops] = (line_entries[amount_of_damage_crops])
                data.append(line_entries)
            except ValueError: print("Error: skipping line", line_count)
            f.close()
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
    return data
#Compiles and prints data in a list of lists
def compileFile(filename):
    file = open(filename, "r")
    csv_reader = csv.reader(file)
    lists_from_csv = []
    for row in csv_reader:
        lists_from_csv.append(row)
        #print(lists_from_csv)
        #print()
    return lists_from_csv
#This function finds the difference in direct deaths to injuries in the list of list.
def difference_in_direct(data):
    count = 0
    for i in range (len(data)):
        count = i
        direct_deaths = int(data[i][8])
        direct_injuries = int(data[i][10])
        difference = direct_deaths - direct_injuries
        print("Storm number:", count, "Direct deaths:", direct_deaths, "Direct injuries:", direct_injuries)
        if(direct_deaths > direct_injuries):
            print("There were more deaths than injuries")
        elif(direct_deaths < direct_injuries):
            print("There were more injuries than deaths")
        else:
            print("There were the same amount of deaths as injuries")
        if(math.fabs(difference) <= 1):
            print("There was no differences between the difference in deaths and injuries ")
            print()
        elif(math.fabs(difference) >= 5):
            print("There was a significant change between the difference of deaths and injuries ")
            print()
        elif (difference < -1):
            print("There was few changes between the difference in deaths and injuries ")
            print()
        elif (difference > 1):
            print("There was more changes between the difference in deaths and injuries ")
            print()
# Q4: In inputted storm, how many storms have at least that amount of crop damage or property damage.
# Find the amount of storms that have caused (at least) that amount of damage (either crop or property)

def crop_property_damage(data):
    count = 0
    entry = 0
    choice = input("property damage or crop damage? ")
    choice.strip().lower()
    num = int(input("Enter a number for the amount of crop or property damage "))
    if (choice == "crop"):
        entry = amount_of_damage_crops
    elif (choice == "property"):
        entry = amount_of_damage_property
    else:
        print("invalid option, please try again")
        # The <= can be changed to == to find any storm has that exact amount of crop damage
        #No storm has between 0 and 999 crop damage
    for i in range (len(data)):
            if(int(data[i][entry]) <= num):
                count +=1
    return "There are", count, "out of", len(data), "storms with at least", num, choice, "damage"
#This function calculates the average length of each type of storm (in days)
def stormAverage(data):
    type_of_storm = input("Enter storm type ")
    avg = 0
    num_of_days = 1
    storm_counter = 0
    for i in range (len(data)):
        start_date = int(data[i][0])
        start_day = int(data[i][1])
        end_date = int(data[i][3])
        end_day = int(data[i][4])

        if(type_of_storm == data[i][7]):
            storm_counter += 1
            storm_length_day = end_day - start_day
            num_of_days += storm_length_day
    if(storm_counter == 0 ):
        print("Division by zero, please try again")
        type_of_storm = input("Enter storm type ")
    else:
        avg = num_of_days / storm_counter
        avg = round(avg, 2)
        return avg
#This function creates the graph for the levels of property damage.
def property(data):
    no_damage = 0
    low_damage = 0
    moderate_damage = 0
    high_damage = 0
    for i in range (len(data)):
        property_damage = int(data[i][12])
        if(property_damage == 0 ):
            no_damage+=1
        elif(property_damage < 1000):
            low_damage+=1
        elif(property_damage > 1000 and property_damage < 10000):
            moderate_damage+=1
        elif(property_damage > 10000):
            high_damage+=1

    x = [no_damage, low_damage, moderate_damage, high_damage]
    labels = ["No Damage", "Low Damage", "Moderate Damage", "High Damage"]
    y = np.arange(len(labels))
    plt.bar(y, x, align="center", alpha=0.5)
    plt.xticks(y,labels)
    plt.ylabel("Number of Storms")
    plt.title("Storm Damage Levels")
    plt.show()
    return "Storms with no damage:", no_damage, "Storms with low damage", low_damage, "Storms with moderate damage", moderate_damage, "Storms with high damage", high_damage

def main():
   stormData = compileFile("storm2000.csv")
   difference_in_direct(stormData)
   numOfStorms = crop_property_damage(stormData)
   print(numOfStorms)
   average = stormAverage(stormData)
   print("The average number of days this storm lasted is:", average, "days")
   print(property(stormData))


main()