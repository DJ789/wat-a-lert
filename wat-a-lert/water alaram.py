import RPi.GPIO as GPIO
import time

# Set the GPIO pins for trigger and echo
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# Set the GPIO pins for the buzzer and LED
GPIO_BUZZER = 17
GPIO_LED = 27

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins as output
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)

# Set the GPIO pins as input
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Set the trigger to low
GPIO.output(GPIO_TRIGGER, False)

def measure_distance():
    # Send a 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Record the time when the echo is received
    start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Record the time when the echo is sent back
    stop_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calculate the distance based on the time difference and the speed of sound
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

while True:
    distance = measure_distance()
    print("Distance: %.1f cm" % distance)

    # If the distance is less than 10 cm, turn on the LED and buzzer
    if distance < 10:
        GPIO.output(GPIO_LED, True)
        GPIO.output(GPIO_BUZZER, True)
    else:
        GPIO.output(GPIO_LED, False)
        GPIO.output(GPIO_BUZZER, False)

    time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()
