import datetime
import random
import time
import json


def chatbot():
    response = "yes"
    while response == "yes":

        question = input("What's that your question sef?\n").split()

        a = open("C:/Users/Public/Documents/insert.json")
        dictionary = json.load(a)

        # dictionary = {
        #     "mood": ["Happy", "grumpy", "sad", "terrible", "upbeat", "angry"],
        #     "time": ["The time is " + str(datetime.datetime.now().time()), "Let me get back to you on that"],
        #     "name": ["Siri", "Jay", "Alexa", "I like you"],
        #     "love": ["I love you!", "Do not fall in love", "Scheiße", "Love is wicked"],
        #     "eat": ["Yeah, lol!", "Nah, I'm fasting "
        #                           "😢"],
        #     "single": ["I'm a single pringle ", "It's like I'm in one relationship like that joor"],
        #     "programs": ["I write python sometimes", "I'm learning java", "I can't kill myself on golang",
        #                  "C# is unnecessarily hard"],
        #     "country": ["I've been to Canada", "Maybe the UK", "Lovely Kenya", "Extremely beautiful Latvia"],
        #     "age": ["I am ", str(random.randint(1, 100)), " years old"],
        #     "play": ["It depends tho", "Biko leave me alone joor", "Let's play then!"],
        #     "sleep": ["I rarely sleep mehn", "I can't shutdown, I can only have a 10sec power nap daily"]
        # }

        reply = []

        question = [x.lower() for x in question]

        if ["exit"] == question:
            print("Exiting...")
            break

        for key in question:
            if key in dictionary.keys():
                reply.append(random.choice(dictionary[key]))

            if reply:
                print(random.choice(reply))
            else:
                print("Ogbeni, don't stress me.... Ask better question biko!")

        time.sleep(1)
        print()

        response = input("Do you want to chat more? (yes or no)\n").lower()
        if response == 'no':
            print("Bye!")


chatbot()
