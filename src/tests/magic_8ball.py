import random

name = input("What is your name? ")
ask_que = input("Hi " + name + ", What is your question? ")
answers = [
    "It is certain.", "It is decidely so.", "Without a doubt.", "Yes definitely!", "You may rely on it.", "As I see it, yes.", "Most likely", "Outlook good", "Yes.", "Signs point to yes", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Dont count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."
]
if (ask_que):
    print(random.choice(answers))

# Made a 'name' variable to ask for name input
# AFTER name is put in, a variable 'ask_que' displays an input to get user to ask a question
# Made a 'answers' variable that has a list value with 20 list items/strings
# IF theres a question in 'ask_que' input
    # OUTPUT random item/string from 'answers' list