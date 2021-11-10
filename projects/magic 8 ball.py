import random
import time

responses = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Replay hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

eight_ball_response = random.choice(responses)

user_question = input("What do you want to the ask the magic 8-ball? ")
print("Thinking...")
time.sleep(2)
print(eight_ball_response)
