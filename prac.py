import csv


with open("students.csv", "w")as file:
    writer = csv.writer(file)
    writer.writerow(["name", "home"])
    name = input("Name: ")
    home = input("Home: ")
    writer.writerow([name, home])


