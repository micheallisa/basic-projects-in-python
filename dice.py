import random
import time

print("\n This will roll a  dice")
time.sleep(2)
how_many_times_to_roll = int(input("How many time do you want  the dice to roll: "))
how_many_sides = int(input("How many sides will the die have? "))
x = 1
while x != how_many_times_to_roll:
    number = random.randint(1, how_many_sides)
    print(number)
    x = x + 1
