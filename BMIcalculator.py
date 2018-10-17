import time

while True:
    try:
        name = input('Hello, what is your name? ')
        if name.isalpha() and len(name) > 2:
            break
        else:
            raise TypeError
    except TypeError:
        print ('Please enter more than 2 characters and use letters only.')

print()
print ('Hi ', name,', nice to meet you!')
time.sleep(1)
print()
print('Do you want to know your BMI?')
time.sleep(1)
print()

def YorN():
    answer = ''
    while answer != 'yes' and answer != 'y' and answer != 'no' and answer != 'n':
        print ('Please type: "yes" or "no" ')
        answer = input()
        continue
    else:
        print('Alright!')
    return answer

answer = YorN()
if answer == 'yes' or answer == 'y': #if 'yes'.startswith(answer): <= another option
    while True:
        try:
            weight = int(input('What\'s your weight? '))
            break
        except ValueError:
            print('Please enter a number.')
        try:
            
elif answer.startswith('n'):
    print ('Have a nice day!')
    time.sleep(2)
    exit()



print('ok')








