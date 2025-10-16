import csv


with open("forest.jpeg", "rb")as file:
    data = file.read()
    lessdata = data[:]
with open("new.jpeg", 'wb') as f:
    f.write(lessdata)
