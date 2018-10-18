import time

while True: #ask user for name and check if properly entered
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

def YorN(): #ask for answer 
    answer = ''
    while answer != 'yes' and answer != 'y' and answer != 'no' and answer != 'n':
        print ('Please type: "yes" or "no" ')
        answer = input()
        continue
    else:
        print('Alright!')
    return answer

answer = YorN() #check an answer and act accordingly
if answer == 'yes' or answer == 'y': #if 'yes'.startswith(answer): <= another option
    while True:
        try:
            weight = float(input('What\'s your weight in range 0 - 250kg? >>> ')) #check if weight is a number in range 0 -250
        except ValueError:
            print('Please enter a number.')
        else:
            if 0.0 < weight < 251.0:
                break
            else:
                print('It\'s not in range!')
elif answer.startswith('n'):
    print ('Have a nice day!')
    time.sleep(2)
    exit()

while True:
    try:
        height = float(input('What\'s your height in centimeters? >>>')) #check if height is a number
        break
    except ValueError:
        print ('Use numbers only!')
height = height / 100 #convert number to height in meters with 2 decimal places
print ('Ok, I\'ve got all data needed.')
time.sleep(1)
print ('Now to count your BMI (Body mass index) I will divide your weight which is:', str(weight) + 'kg by your height:', str(height) + 'm.')
print()
wh = round((weight / height),2) #calculate BMI
time.sleep(2)
print ('It gives us', str(wh) +'.')
print()
time.sleep(1)
print ('The result I will divide again by your height.')
time.sleep(1)
print ('So, we have your BMI!')
print()
bmi = wh / height
bmi = round(bmi,2)
time.sleep(1)
print ('It is', str(bmi)+ '!!!')

time.sleep(2) #depend on BMI give an opinion
if 18.5 >= bmi:
    print ('It means that you are underweight. Try to eat a bit more and get some weight ;)')
elif 18.5 < bmi <= 24.9:
    print ('It means that you are normal. Keep it up!')
elif 24.9 < bmi <= 29.9:
    print ('It means that you are overweight! That\'s not good. Try to eat less, do some exercises.')
    time.sleep(1)
    print ('It\'s about your health and life!')
elif 30 <= bmi:
    print ('Your situation is serious. You are really obese!')
    time.sleep(1)
    print('You have to lose weight man!!! Really, think about it.')

time.sleep(2)
print()
print('Take care and thanks for using this BMI calculator!')
time.sleep(3)
exit()


