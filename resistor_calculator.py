# RESISTOR COMBINATION CALCULATOR
print("RESISTOR COMBINATION CALCULATOR")

# Ask for a valid number of resistors 
while True:
    try: 
        number_of_resistors = int(input("How many resistos do you have?"))

        if number_of_resistors >0: break
        else:
            print("please enter a number greater than zero.")
    except ValueError:
        print("Invalid input! please enter a whole number.")

# Create an empty list 
resistor_values = []

# Collect resistor values
for i in range (number_of_resistors):
    while True: 
        try:
            resistance = float(input("Enter resistor value in ohms: "))
            if resistance > 0:
                resistor_values.append(resistance) 
                break
            else:
                print("Resistance must be greater than zero.")
        except ValueError:
            print("Invalid input! please enter a number.")

#Display the resistor value
print("Your resistor values are:",resistor_values)

# Function to calculate total resistance in series
def calculate_series(resistors):
    total = 0

    for resistance in resistors : 
        total = total + resistance

    return total

#Calculate series resistance
series_total = calculate_series(resistor_values)

#Display the result 
print ("Total resistance in series:",round (series_total, 2),"ohms")

# Function to calculate total resistance in parallel
def calculate_parallel(resistor):
    total = 0
    for resistance in resistor:
        total= total+ (1/resistance)

    return 1/total

# Calculate parallel resistance 
parallel_total = calculate_parallel(resistor_values)

#Display the result
print("Total resistance in parallel:", round (parallel_total,2),"ohms") 

# Compare series and parallel resistance 
if series_total > parallel_total:
    print("series resistance is higher.")
elif parallel_total > series_total:
    print ("parallel resistance is higher.")
else:
    print("Both resistance are equal.")

# Display final calculation summary
print("\n================================")
print("CALCULATION SUMMARY")
print("===============================")

print("Number of resistors:", number_of_resistors)
print("resistor value:", resistor_values)

print("--------------------------------")
print("Series Resistance:", round(series_total, 2),"ohms")
print("Parallel Resistance:",round(parallel_total, 2), "ohms")
print("--------------------------------")

print("Series resistance is higher.")
print("Thank you for using my calculator!")
print("===============================")