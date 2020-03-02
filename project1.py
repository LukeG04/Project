
#For my project I will ask the user for a produce item from the grocery store and the quantity. Then I will calculate the cost of that item and print to the user the total cost of all of their produce items in the basket.

#Simple function for introducing the costumer to King Soopers
def introduce():
  print("Welcome to King Soopers!")

#More complicated function finding the cost of the product
def cost(price):
  pCost = int
  pCost = price * number
  return pCost
#Call introduction function
introduce()
#Ask user if they have any produce items
yesNo = str(input("Do you have any produce items you wish to buy? (Yes or no)\n"))
#While they do have any produce items then run this if statement else print to user the total cost.
totalCost = 0
if(yesNo == "yes"):
  while(yesNo == "yes"):
    #Get user input on the type of product.
    userProduce = str(input("What item do you wish to buy? (apples, bananas, limes, oranges, strawberries, red grapes, or green grapes)\n"))
    #Get user in[ut for the quantity of that produce that they wish to buy.
    number = int(input("How many %s do you wish to buy?\n" %(userProduce)))
    #Get prices for each product
    if(userProduce == "apples"):
      price = 1.95
    elif(userProduce == "bananas"):
      price = 0.30
    elif(userProduce == "limes"):
      price = 0.50
    elif(userProduce == "oranges"):
      price = 0.89
    elif(userProduce == "strawberries"):
      price = 2.50
    elif(userProduce == "red grapes" or userProduce == "green grapes"):
      price = 3.98
    else:
      print("I'm sorry we don't carry that here.\n")
      print("Please get help from an assistant.\n")
      break
    #Call function to find the price of the product they wish to buy
    cost(price)
    #Printing to the user the cost
    print("Your %s cost %.2f" %(userProduce, cost(price)), "\n")
    #Adding up to the final cost for the end of the program
    totalCost = totalCost + cost(price)
    #Asking if they want more product and if they don't then don't run the code again.
    yesNo = str(input("Do you want to buy more produce?\n"))
#Printing to the user the total cost of their trip to the store
print("The total cost of your trip today is $%.2f" %(totalCost))


