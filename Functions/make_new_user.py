import csv
import os


with open("Data/users.csv", "a") as f:
    writer = csv.writer(f)

    num = int(input("Add How Many Users?"))
    for i in range (num):
        name = input("Name: ")
        password = input("Password: ")
        
        writer.writerow([name, password])
