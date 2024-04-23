# Name: Igor Andriesii
# Student no.: B00145876
# Description: To detect motion using the PIR sensor

from periphery import GPIO
import time

pir_pin = 154

try:
    print("PIR Module Test")
    pir = GPIO(pir_pin, "in")

    while True:
        if pir.read():
            print("Motion Detected!")
            time.sleep(1)
        else:
            print("No Motion Detected!")
            time.sleep(1)

#time.sleep(10) -- temporary line of code (used for testing)

except KeyboardInterrupt:
        print("Exiting...")
        pir.close()
