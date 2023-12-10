#Empty py intended as a suggestion for a type of event a student could add. For ease of merging, students should append their names or other id to this py and any classes, to reduce conflicts.
from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Fishing_Game(Context, event.Event):
    def __init__(self):
        super().__init__()
        self.name = "fishing spot"
        self.keys = 0
        self.verbs = {
            'catch': self,
            'quit': self
        }
        self.result = {}
        self.go = True  
        self.inwater = ["ArenaKey", "tuna", "boot", "hering", "squid"]

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "catch":
            self.catch()
        elif verb == "quit":
            self.quit_fishing()

    def catch(self):
        caught = random.choice(self.inwater)
        self.inwater.remove(caught)
        print(f"You caught a {caught}!")
        if caught == "ArenaKey":
            print(f"You found an ArenaKey")
            self.keys += 1

    def quit_fishing(self):
        self.result["message"] = "You decide to stop fishing."
        self.go = False

    def process(self, world):
        self.result = {}
        self.result["newevents"] = [self]
        self.result["message"] = "Welcome to the fishing spot. What do you want to do?"
        print(self.result["message"])

        while self.go:
            print(f"{len(self.inwater)} items in the water. What do you want to do?")
            Player.get_interaction([self])

        return self.result