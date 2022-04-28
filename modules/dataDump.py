import csv
import datetime

#fields = ["Date/Time", "temperature", "Moisture", "Humidity", "Light", "Height"]

def writeValues(temperature,moisture,humidity,light,height):
    file="./PlantData.csv"

    with open(file, "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        current_time = datetime.datetime.now()
        
        row=[current_time,temperature,moisture,humidity,light,int(height)]
        print(row)
        csvwriter.writerow(row)
        #csvfile.close()
