from classes import Hardware
import schedule
import smtplib
import time
import ssl

SECONDS_TO_WATER = 10
RELAY = Hardware.Relay(12, False)

def water_plant(relay, seconds):
    relay.on()
    print("Plant is being watered!")
    time.sleep(seconds)
    print("Watering is finished!")
    relay.off()

while True:
    time.sleep(1)
    water_plant(RELAY, SECONDS_TO_WATER)
