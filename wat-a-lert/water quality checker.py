# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Set up GPIO pins for TDS meter
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

def get_TDS():
    # Turn on TDS meter
    GPIO.output(23,GPIO.HIGH)
    
    # Wait for sensor to stabilize
    time.sleep(2)
    
    # Measure TDS
    GPIO.output(23,GPIO.LOW)
    start = time.time()
    while GPIO.input(24)==0:
        start = time.time()
    while GPIO.input(24)==1:
        end = time.time()
    duration = end-start
    TDS_value = (duration * 1000) / 6
    
    # Turn off TDS meter
    GPIO.output(23,GPIO.LOW)
    
    return TDS_value

# Get TDS reading
TDS = get_TDS()

# Check TDS reading against threshold for water quality
if TDS < 500:
    print("Water quality is good.")
else:
    print("Water quality is poor. Please consider filtering or treating the water.")
