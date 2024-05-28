import random
import requests
import time

amount = input("How many numbers do you want to sort: ")
while not amount.isdigit():
    print("Please enter a valid number")
    amount = input("How many numbers do you want to sort: ")

amount = int(amount)

while int(amount) > 100:
    print("Please enter a number at or below 100")
    amount = input("How many numbers do you want to sort: ")

response = requests.get(f"http://www.randomnumberapi.com/api/v1.0/random?min=0&max=100&count={amount}")
dataObj = response.json()
i = 0
for data in dataObj:
    RandKeyList = []
    RandKeyList.append(dataObj[i])
    i+= 1
print("Start values: " + ', '.join(map(str, dataObj)))


class action(): 
    def __init__(self, data):
        global dataObj
        self.data = data
    change = input("Are you happy with the values. Enter if happy 'No' if you want to change: ")
    if change == "No":
        response = requests.get(f"http://www.randomnumberapi.com/api/v1.0/random?min=0&max=100&count={amount}")
        dataObj = response.json()
        i = 0
        for data in dataObj:
            RandKeyList = []
            RandKeyList.append(dataObj[i])
            i+= 1
        print("New values: " + ', '.join(map(str, dataObj)))
        print(str, dataObj)
    else:
        print("Values are the same")


class bogo():
        import random
        def __init__(self, data=None):
            global dataObj
            self.data = dataObj if data is None else data
            print(str, dataObj)
        def is_sorted(self, data):
            return all(self.data[i] <= self.data[i+1] for i in range(len(self.data)-1))
        def bogo_sort(self):
            ct = 0
            while not self.is_sorted(self.data):
                random.shuffle(self.data)
                ct += 1
                print(', '.join(map(str, self.data)), f" ||  Counter: {ct}")
            return', '.join(map(str, self.data)) + f"  ||  It took {ct} attempts"

input("Press Enter to start the function below")
sorter = bogo(dataObj)
print(sorter.bogo_sort())