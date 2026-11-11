
# ND1 MECHATRONICS ENGINEERING
# Temperature Monitor and Alarm Checker

# Function to collect valid temperature readings
def get_number(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a positive temperature.")
            else:
                return value

        except ValueError:
            print("Invalid input! Enter a number.")


# Function to monitor machine temperature
def monitor_temperature():

    readings = []

    print("\nWELCOME TO TEMPERATURE MONITOR")

    # Collect five temperature readings
    for i in range(5):
        temp = get_number(
            "Enter temperature reading " + str(i + 1) + ": "
        )
        readings.append(temp)

    # Collect safe temperature limit
    safe_limit = get_number("Enter safe temperature limit: ")

    # Calculate temperature results
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- TEMPERATURE REPORT ---")
    print("Highest:", highest, "°C")
    print("Lowest:", lowest, "°C")
    print("Average:", round(average, 2), "°C")

    # Check temperature safety
    alarm_count = 0

    for temp in readings:
        if temp > safe_limit:
            print("WARNING! High temperature:", temp, "°C")
            alarm_count += 1
        else:
            print("Temperature is safe:", temp, "°C")

    # Display machine condition
    if alarm_count == 0:
        print("Machine Status: NORMAL")
    elif alarm_count <= 2:
        print("Machine Status: WARNING")
    else:
        print("Machine Status: DANGER")

    # Extra feature: Check temperature trend
    if readings[-1] > readings[0]:
        print("Temperature Trend: RISING")
    elif readings[-1] < readings[0]:
        print("Temperature Trend: FALLING")
    else:
        print("Temperature Trend: STABLE")


# Main program
while True:

    monitor_temperature()

    again = input("\nCheck another machine? (yes/no): ").lower()

    if again == "no":
        print("Thank you for using the program!")
        break
    elif again == "yes":
        continue
    else:
        print("Invalid choice. Program ended.")
        break
