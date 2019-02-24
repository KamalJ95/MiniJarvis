import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "wait", "cancel"]

    def respond(self, response):
        print(response)
        os.system("say  " + response)

    def discover(self, text):
        if "what" in text and "your name" in text:
                self.respond('its ya boy kevin sam')
        if "my" in text:
            self.respond('You havent told me your name yet')
        if "life" in text:
            self.respond('42')





