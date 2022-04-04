import csv
import datetime

# field names
fields = ["Date/Time", "temperature", "Moisture", "Humidity", "Light", "Height"]

# initialising the csv file
file = "HornyPlant.csv"
with open(file, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    while True:
        row = []
        current_time = datetime.datetime.now("Asia/Kolkata")
        row.append(current_time)
        # insert sensor codes here
        row.append()
        csvwriter.writerow(csvfile)
