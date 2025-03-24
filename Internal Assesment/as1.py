"""Creating a program to ask the speed of the space probe. If the speed that has been inputed is valid, it will add it to the list. 
Finally at the end of the program, it will go through all the speeds in the list, print the amount of speeds over the limit and print the speeds which were over the limit."""

# Creating a list to store the speeds. 
speed = []
highspeeds = 0 
HIGH = 10  # maximum safe speed.
SMALL = 0
stop = 'done' # stops program if the user inputs 'done'.
meter_sec = input('Input descent speed in m/s: ')
while meter_sec != stop:
    try:
        meter_sec = meter_sec.lower()
        if meter_sec.strip('.').isnumeric():
            speed.append(float(meter_sec))
        else:
            print('Error, invalid input.')
        meter_sec = input('Input descent speed in m/s: ')
        meter_sec = meter_sec.lower()
    except ValueError:
        print('Error, invalid input.')
for item in speed:
    if item > HIGH:
        highspeeds = highspeeds + 1
print(f"There were {highspeeds} space probes faster than the safe speed.")
if highspeeds > SMALL:
    print('The unsafe speeds are')
    for item in speed:
        if item > HIGH:
            print(item)