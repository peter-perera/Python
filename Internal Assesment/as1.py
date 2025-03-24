"""Creating a program to ask the speed of the space probe. If the speed that has been inputed is valid, it will add it to the list. 
Finally at the end of the program, it will go through all the speeds in the list, print the amount of speeds over the limit and print the speeds which were over the limit."""

# Creating a list to store the speeds. 
speed = []
HIGH = 10  # maximum safe speed.
SMALL = -1
stop = 'done' # stops program if the user inputs 'done'.
meter_sec = float(('Input descent speed in m/s: '))
while meter_sec != stop:
    try:
        