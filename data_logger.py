import random
import time

# Function to generate simulated temperature data
def generate_temperature():
    
    # Round the generated temperature value to two decimal places
    return round(random.uniform(-20, 40), 2)

# Main function for logging temperature data
def main():
    print("Temperature data logging is starting.")
    while True:
        temperature = generate_temperature()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
#This line opens the file "temperature_log.txt" in "append" mode using a with statement. 
#The "a" mode means that the file is opened for appending new data to the end of the file, 
#and if the file doesn't exist, it will be created.


        with open("temperature_log.txt", "a") as file:
            # represents the Unicode escape sequence for the degree symbol (°), and it's used to correctly include the degree symbol in the string.
            file.write(f"{timestamp}: {temperature}\u00b0C\n")

        
        time.sleep(5)  # Adjust the interval (in seconds) as needed

if __name__ == "__main__":
    main()