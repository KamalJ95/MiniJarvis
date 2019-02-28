import subprocess
import os
import random
from answer import Fetcher


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
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)










