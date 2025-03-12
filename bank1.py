#entering variables
start = 200
balance = 200
small = 0
balance_list = []
# input and calculations
while True:
    try: 
        spent = int(input('Enter the amount spent: '))
        while balance >= small:
            balance = balance - spent
            balance_list.append(balance)
            if spent >= start:
                balance = balance - spent
                balance_list.append(balance)
                print('My bank balances have been:')
                print(start)
                for item in balance_list:
                    print(item)
                exit()
            else:
                 while spent > small:
                    balance = balance - spent
                    balance_list.append(balance)
                    spent = int(input('Enter the amount spent: '))
        break
    except ValueError:
        print('Not a valid amount.')
print('My bank balances have been:')
print(start)
for item in balance_list:
    print(item)