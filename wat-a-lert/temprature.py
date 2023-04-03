import os

# Set the ID of the temperature sensor
sensor_id = '28-01131a4b9c05'

# Define a function to read the temperature from the sensor
def read_temperature():
    # Open the file that contains the temperature data
    file_path = '/sys/bus/w1/devices/{}/w1_slave'.format(sensor_id)
    file = open(file_path, 'r')
    
    # Read the temperature data from the file
    lines = file.readlines()
    file.close()
    
    # Check if the temperature data is valid
    if lines[0].strip()[-3:] != 'YES':
        return None
    
    # Extract the temperature value from the data
    temperature_data = lines[1].strip().split('=')[1]
    temperature = float(temperature_data) / 1000.0
    
    return temperature

# Read the temperature from the sensor
temperature = read_temperature()

# Print the temperature to the console
if temperature is not None:
    print('Temperature: {:.2f} degrees Celsius'.format(temperature))
else:
    print('Error: Could not read temperature data')
