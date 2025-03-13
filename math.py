smart = 0 # input storage.
smart_list = []
small = 79
high = 100
stop = 'done'
score = input("Enter a score, or type 'done' to exit: ")
while score != stop:
    try:
        score = score.lower()
        if score.isnumeric():
            smart_list.append(int(score))
        else:
            print('Invalid score!')
        score = input("Enter a score, or type 'done' to exit: ") 
    except ValueError:
        print('Invalid score!')
for item in smart_list:
    if item > small:
        smart = smart + 1
if smart == 1: #output
    print("This class has 1 smart student!")
elif smart > 1:
    print(f"This class has {smart} smart students!")
else:
    print('This class has 0 smart students!')