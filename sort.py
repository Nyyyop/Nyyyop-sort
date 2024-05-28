# Import necessary libraries
import random
import requests
import time

# Ask the user for the amount of numbers they want to sort
amount = input("How many numbers do you want to sort: ")

# Validate the input to ensure it's a digit
while not amount.isdigit():
    print("Please enter a valid number")
    amount = input("How many numbers do you want to sort: ")

# Convert the input to an integer
amount = int(amount)

# Validate the input to ensure it's at or below 100
while int(amount) > 15:
    print("Please enter a number at or below 15")
    amount = input("How many numbers do you want to sort: ")

# Send a GET request to the Random Number API and get a response
response = requests.get(f"http://www.randomnumberapi.com/api/v1.0/random?min=0&max=100&count={amount}")

# Parse the JSON response and assign it to dataObj
dataObj = response.json()

# Initialize a counter variable
i = 0

# Loop through each item in the dataObj list
for data in dataObj:
    # Initialize an empty list
    RandKeyList = []
    # Append the current item from dataObj to the list
    RandKeyList.append(dataObj[i])
    # Increment the counter
    i+= 1

# Print the initial values in dataObj
print("Start values: " + ', '.join(map(str, dataObj)))

# Define a class named action
class action(): 
    # Define the constructor method
    def __init__(self, data):
        # Declare dataObj as a global variable
        global dataObj
        # Assign the input argument to the data attribute
        self.data = data

# Define a class named bogo
class bogo():
    # Import the random library
    import random
    # Define the constructor method
    def __init__(self, data=None):
        # Declare dataObj as a global variable
        global dataObj
        # If data is None, assign dataObj to the data attribute, otherwise assign the input argument
        self.data = dataObj if data is None else data
    # Define a method to check if the data is sorted
    def is_sorted(self, data):
        # Return True if the data is sorted, otherwise return False
        return all(self.data[i] <= self.data[i+1] for i in range(len(self.data)-1))
    # Define a method to sort the data using the bogo sort algorithm
    def bogo_sort(self):
        # Initialize a counter variable
        ct = 0
        # Initialize a timer
        start_time = time.time()
        time.sleep(0.00000001)
        # While the data is not sorted
        while not self.is_sorted(self.data):
            # Calculate elapsed time
            elapsed_time = round(time.time() - start_time, 5)
            # Shuffle the data
            random.shuffle(self.data)
            # Increment the counter
            ct += 1
        # Print the current state of the data, the counter, and the elapsed time
            # Print the current state of the data and the counter
            print(', '.join(map(str, self.data)), f" ||  Counter: {ct} | Time: {elapsed_time} seconds | Rate: {ct/elapsed_time} attempts per second")
        # Return the sorted data and the number of attempts it took
        return', '.join(map(str, self.data)) + f"  || Took {ct} attempts, {elapsed_time} seconds, rate: {ct/elapsed_time} attempts per second"

# Ask the user to press Enter to start the function below
input("Press Enter to start the function below")

# Create an instance of the bogo class with dataObj as the argument
sorter = bogo(dataObj)

# Print the result of the bogo_sort method
print(sorter.bogo_sort())