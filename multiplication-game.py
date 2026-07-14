import random

name = input("Enter your name , champion!! ")
score = 0

for i in range(5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = int(input(f"{num1} × {num2} = "))
    
    if answer == num1 * num2:
        print("CORRECT!great gob! 👏")
        score += 1
    else:
        print(f"Wrong the answer is {num1*num2}")

print(f"Your final score is  : {score}/5")
