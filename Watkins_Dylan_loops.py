#Tast 1: Count 1 to 12 
for x in range(1, 13):
  print(x)
#Task 2: Sum 1..200 (accumulator, while)
i = 1
x = 0
while i <= 200:
    x += i
    i += 1
print('Sum 1...200= ', x)
#Task 3: Even numbers 0..30
for x in range(0,31,2):
    print(x, end=' ')
#Task 4: Multiplication table
k = int(input("Please enter a number: "))
for x in range(1, 11):
    y = k * x
    print(f"{k} * {x} = {y}")
#Task 5: Read N numbers with validation
while True:
  #establish how many numbers will be entered and confirm it's a positive number
    x = int(input('How many numbers would you like to enter: '))
    if x <= 0:
        print('Please enter a positive number')
        break
      #set a 'blank' starting spot for the variables that will be used later 
    total = 0
    numbers = []
    y = 0
    for y in range(x):
        while True:
            z = int(input(f'Enter number #{y+1}: '))
            numbers.append(z)
            total += z
            break
          #Now that everything is defined given user inputs, this will outline the math we need done to find the average
    average = total / x
    print(f"sum: {total}")
    print(f"average: {average}")
    break
#Task 6: Min/Max until “done”  
#First, set a blank value that will be added to later
x = []
while True:
    userinput = input("Please enter a number or type 'done': ")
  #input needs to be a string so the sytem can accept done as a valid input. Once we establish it's not 'done', we can switch from an string to a interger
    if userinput == 'done':
        break
    else:
        y = int(userinput)
    x.append(y)
if x:
    print(f'Minimum: {min(x)}')
    print(f'Maximum: {max(x)}')
#Task 7: Count vowels in a word
def count_vowels(user_input):
    vowels = "aeiouAEIOU"
    return sum(1 for char in user_input if char in vowels)
user_input = input("Please enter a word: ")
x = count_vowels(user_input)
print(f'vowels: {x}')
#Task 8: Simple stats from a list
Data = [12, 3, 7, 7, 20, -2, 0, 15, 15, 9]
Count = 0
Sum = 0
Minimum = Data[0]
Maximum = Data[0]
for number in Data:
    Count +=1
    Sum += number
    if number < Minimum:
        Minimum = number
    if number > Maximum:
        Maximum = number
        
print(f'Provided Data: {Data}')
print(f'Count: {Count}')
print(f'Sum: {Sum}')
print(f'Minimum Value: {Minimum}')
print(f'Maximum value: {Maximum}')
#Task 9: Number guess
print('Guess the Number!')
import random
x = random.randint(1,10)
attempts = 0
max_attempts = 5
answer = False
while attempts < max_attempts:
    y = int(input('Please make a guess: '))
    attempts += 1
    if x > y:
        print('Too low')
    if x < y:
        print('Too high')
    if x == y:
        print('Correct')
        answer = True
        break
if answer == False:
    print(f'Sorry, the number was {x}')
  #Task 10: Tiny ASCII rectangle
x = int(input('Please enter the height of the rectangle: '))
y = int(input('Please enter the width of the rectangle: '))
for row in range(x):
    if row == 0 or row == x-1:
        print('#' * y)
    else:
        if y > 1:
            print('#'+' ' * (y-2) + '#')
        else:
            print('#')
