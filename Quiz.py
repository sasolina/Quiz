from random import randint
import random
from operator import add,sub,mul
counter = 0
while counter <= 9:
    
    num1 = random.randint(1,10)
    num2 = random.randint(2,10)
    operator = (add,sub,mul)
    choice = random.choice(operator)

    ans = (num1,operator,num2)
    if choice == add:
        print(f'what is, {num1} + {num2}?')
        ans = int(input())
        counter = counter + 1
        print(counter)
      
    elif choice == sub:
      if num1 > num2:
        print(f'what is, {num1} - {num2}?')
        ans = int(input())
        counter = counter + 1
        print(f'your score is {counter}')
      elif num2 > num1:
        print(f'what is, {num2} - {num1}?')
        ans = int(input())
        counter = counter + 1
        print(f'your score is {counter}')
    
    elif choice == mul:
        print(f'what is, {num1} * {num2}?')
        ans = int(input())
        counter = counter + 1
        print(f'your score is {counter}')
        
    if counter == 10:
        print("its the end of game")
        print(f'well done your total score is {counter}')

