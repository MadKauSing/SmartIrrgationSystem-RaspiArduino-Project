import csv
import datetime

#fields = ["Date/Time", "temperature", "Moisture", "Humidity", "Light", "Height"]

def writeValuesTest(temperature,moisture,humidity,light,height):
    file="./PlantData.csv"

    with open(file, "a",newline='') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        current_time = datetime.datetime.now()
        
        row=[[current_time,int(temperature),int(moisture),humidity,int(light),int(height)]]
        print(row)
        csvwriter.writerows(row)
        # csvfile.close()
