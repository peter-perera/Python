"""This program will ask the user for the amount of pizzas that they want out of four choices. Then it will print the amount of pizzas per flavour/topping."""

pizza_list = [] # list to store the amount of pizzas
small = 0

# Go through the list of pizzas in order and asking how many of each pizza. 
while True:
    try:

        cheese = input("How many cheese pizzas do we want? ")
        cheese = int(cheese)
        if cheese == small:
            break
        elif cheese < small:
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
        if chicken == small:
            break
        elif chicken < small:
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
        if pepperoni == small:
            break
        elif pepperoni < small:
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
        if veggie == small:
            break
        elif veggie < small:
            print('Please enter a valid amount.')
        else:
            pizza_list.append(veggie)
            break
    except ValueError:
        print('Please enter a valid amount. ')
