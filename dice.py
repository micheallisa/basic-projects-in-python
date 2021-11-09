import random
import time

print("\n This will roll a 6-sided dice")
time.sleep(2)
how_many_times_to_roll = int(input("How many time do you want  the dice to roll: "))
x = 1
while x != how_many_times_to_roll:
    number = random.randint(1, 6)
    print(number)
    x = x + 1
