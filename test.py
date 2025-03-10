stop = 0
small = 1.2 # min value
volt_list = []
volt = input('Enter your input: ')
if isinstance(volt, (int, float)):
    while volt >= stop:
        volt_list.append(volt)  # adding item to list
        volt = input('Enter your input: ')
else:
    print('Not robot compliant!')
for item in volt_list:
    if item >= small: # comparing 
        print('Beep')
    else:
        print('Boop')