"""This program will ask the user for the amount of pizzas that they want out of four choices. Then it will print the amount of pizzas per flavour/topping."""

pizza_list = [] # list to store the amount of pizzas
small = 0

# Go through the list of pizzas in order and asking how many of each pizza. 
while True:
    try:

        cheese = input("How many cheese pizzas do we want? ")
        cheese = int(cheese)
        if cheese < small:
            print('Please enter a valid amount.')
        else:
            pizza_list.append(cheese)
            break
    except ValueError:
        print('Please enter a valid amount. ')

while True:
    try:

        chicken = input("How many chicken pizzas do we want? ")
        chicken = int(chicken)
        if chicken < small:
            print('Please enter a valid amount.')
        else:
            pizza_list.append(chicken)
            break
    except ValueError:
        print('Please enter a valid amount. ')

while True:
    try:

        pepperoni = input("How many pepperoni pizzas do we want? ")
        pepperoni = int(pepperoni)
        if pepperoni < small:
            print('Please enter a valid amount.')
        else:
            pizza_list.append(pepperoni)
            break
    except ValueError:
        print('Please enter a valid amount. ')

while True:
    try:

        veggie = input("How many veggie pizzas do we want? ")
        veggie = int(veggie)
        if veggie < small:
            print('Please enter a valid amount.')
        else:
            pizza_list.append(veggie)
            break
    except ValueError:
        print('Please enter a valid amount. ')
# printing the amount of each pizza.
#Excluding 0 pizzas
for i in range(0, 1):
    if pizza_list[0] != small:
        print(f"Cheese: {pizza_list[0]}")
    if pizza_list[1] != small:
        print(f"Chicken: {pizza_list[1]}")
    if pizza_list[2] != small:
        print(f"Pepperoni: {pizza_list[2]}")
    if pizza_list[3] != small:
        print(f"Veggie: {pizza_list[3]}")