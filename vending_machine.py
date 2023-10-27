#vending machine
# 1. put a few drinks (array of dictionary)
drinks = [{"itemId": 0, "itemName":"coke", "itemCost":2.0},{"itemId": 1, "itemName":"Milo", "itemCost": 3.0}, {"itemId": 3 ,"itemName":"Mineral_Water","itemCost":1.0}]

# put the drink into this list 
item = []
# put the string of the receipt inside
reciept = ""
# totalCash
totalCash = 0

# create a receipt to print out
def createReceipt(item, reciept):
   for i in item:
      reciept += f'{i["itemName"]} -- {i["itemCost"]}'
   reciept += f"\nTotal --- {sumItem(item)}"
   return reciept

# get the value
def sumItem(item):
   sumItems = 0
   for i in item:
      sumItems += i["itemCost"]
   return sumItems


# 2. Only Notes (no coin)
# 50, 20 , 10, 5, 1
def getIdealChange(item,totalCash):
    tally = {
        "fifty": 0,
        "twenty": 0,
        "ten": 0,
        "five": 0,
        "one": 0
    }

    changeDue = totalCash - sumItem(item)
    
    while (changeDue >= 50):
        tally["fifty"] += 1
        changeDue -= 5
    while (changeDue >= 20):
        tally["twenty"]+=1
        changeDue -=20
    while changeDue >= 10:
        tally["ten"]+=1
        changeDue -= 10
    while changeDue >= 5:
        tally["five"] +=1
        changeDue -= 5
    while changeDue >= 1:
        tally["one"] +=1
        changeDue -= 1 
    return tally


# Insert an item
buyItem = int(input("Enter the item code for the drinks: "))
if buyItem < len(drinks):
    item.append(drinks[buyItem])
    print(createReceipt(item, reciept))
# Insert Money
totalCash = int(input("Insert Money: "))
# Get changes
print(getIdealChange(item,totalCash))




