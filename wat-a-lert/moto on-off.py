import datetime
import time

# Define motor on time
motor_on_time = datetime.time(hour=6, minute=0)   # Motor turns on at 6:00 AM

# Define motor on duration in seconds
motor_on_duration = 1800  # Motor runs for 30 minutes (1800 seconds)

# Main loop
while True:
    # Get current time
    now = datetime.datetime.now().time()
    
    # Check if it's time to turn the motor on
    if now == motor_on_time:
        print("Reminder: Turn motor on!")
        motor_start_time = time.time()  # Record the start time of the motor
        
        # Wait for the motor to run for the specified duration
        while (time.time() - motor_start_time) < motor_on_duration:
            time.sleep(1)
        
        # Turn motor off after specified duration
        print("Reminder: Turn motor off!")
    
    # Wait 1 minute before checking again
    time.sleep(60)  # 60 seconds = 1 minute
