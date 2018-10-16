while True:
    try:
        name = str(input('Hello, what is your name? '))
        break
    except ValueError:
        print ('Please use letters only.')

print()
print ('Hi ' +name+ ', nice to meet you!\nDo you want to know your BMI?')

print()
answer = ''
while answer != 'Yes' and answer != 'yes' and answer != 'No' and answer != 'no':
    answer = input('Please type: "Yes" or "No"? ' )


if answer == 'Yes' or 'yes':
    while True:
        try:
            weight = int(input('What is your weight? '))
            while True:
                weight = int(input('Please enter a number in range 0 to 250. '))
                if 0 <= weight <= 250:
                    break
                else:
                    continue
            break
        except ValueError:
            print ('Please enter a number in range 0 to 250.')






'''elif answer == 'No' or 'no':
    print ('Ok, no problem. Have a nice day!')
else:
    print ('Simply write "Yes" or "No"')

weight = input()

height = input('And what is your height? ')
'''
