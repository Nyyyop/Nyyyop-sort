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
class bogo():
    import random
    def __init__(self, data=None):
        global dataObj
        self.d = dataObj if data is None else data
    def i(self, data):
        return all(self.d[i] <= self.d[i+1] for i in range(len(self.d)-1))
    def bogo_sort(self):
        ct = 1
        st = time.time()
        et = 0
        while not self.i(self.d):
            et = time.time() - st
            random.shuffle(self.d)
            ct += 1
        return', '.join(map(str, self.d)) + f"  || Took {ct-1} attempts, {round((et+0.00000000000000000001), 4)} seconds, rate: {round((ct-1)/(et+0.00000000000000000001), 1)} attempts per second"
input("Press Enter to start the function below")
sorter = bogo(dataObj)
print(sorter.bogo_sort())