import csv
import datetime

fields = ["Date/Time", "temperature", "Moisture", "Humidity", "Light", "Height"]
file="../PlantData.csv"

with open(file, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)