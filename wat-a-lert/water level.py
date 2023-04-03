import RPi.GPIO as GPIO

# Set the GPIO pin number to use for the water level sensor
water_level_pin = 18

# Set up the GPIO pin for input
GPIO.setmode(GPIO.BCM)
GPIO.setup(water_level_pin, GPIO.IN)

# Read the water level sensor data
water_level = GPIO.input(water_level_pin)

# Send the water level data to the viewer app
send_data_to_viewer_app(water_level)
