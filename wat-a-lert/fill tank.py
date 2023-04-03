import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers to use for the ultrasonic sensor
trigger_pin = 23
echo_pin = 24

# Set up the GPIO pins for the ultrasonic sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

# Set the dimensions of the tank in centimeters
tank_height = 50
tank_width = 30
tank_length = 40

# Calculate the volume of the tank in cubic centimeters
tank_volume = tank_height * tank_width * tank_length

# Set the threshold water level that indicates the tank is full
full_water_level = tank_volume

# Define a function to measure the distance using the ultrasonic sensor
def measure_distance():
    # Send a 10 microsecond pulse to the ultrasonic sensor
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    # Measure the duration of the echo pulse
    start_time = time.time()
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()
    while GPIO.input(echo_pin) == 1:
        end_time = time.time()

    # Calculate the distance based on the duration of the echo pulse
    pulse_duration = end_time - start_time
    distance = pulse_duration * 17150
    return distance

# Continuously measure the distance and calculate the water level
while True:
    distance = measure_distance()
    
    # Calculate the water level based on the tank's dimensions and the distance
    tank_area = tank_width * tank_length
    water_height = tank_height - distance
    water_volume = tank_area * water_height
    water_level = int(water_volume)

    if water_level >= full_water_level:
        # Send an alert to the user through the viewer app
        send_alert_to_user_app("Tank is full!")
        break
