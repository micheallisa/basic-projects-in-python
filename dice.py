import random
import time

# Allows the user to input the times the dice will roll and the amount of sides it has
print("\n This will roll a  dice")
time.sleep(2)
how_many_times_to_roll = int(input("How many time do you want  the dice to roll: "))
how_many_sides = int(input("How many sides will the die have? "))

# Creates a loop that rolls the dice the amount of times the user inputed, and then stops when that number is reached
x = 1
while x != how_many_times_to_roll:
    number = random.randint(1, how_many_sides)
    print(number)
    x = x + 1
