import subprocess
import os
import random


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "wait", "cancel"]

    def respond(self, response):
        print(response)
        os.system("say  " + response)

    def discover(self, text):
        if "what" in text and "your name" in text:
                self.respond('My name is Jarvis')
        if "my" in text:
            self.respond('You havent told me your name yet')
        if "life" in text:
            self.respond('42')
        if "random" in text:
            target = random.randrange(0,6)
            self.respond(self.confirm[target])







