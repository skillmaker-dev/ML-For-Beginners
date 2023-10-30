import random

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

close = False

while not close :
    inp = input("\n" + random_responses[random.randint(0,5)] + "\n>")
    if inp == "exit":
        break