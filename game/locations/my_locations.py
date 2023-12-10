from game import location
import game.config as config
from game.display import announce
from game.events import *
from game.items import *
from game.events.fish import FishGame

class Island(location.Location):
    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "island"
        self.symbol = 'Y'
        self.visitable = True
        self.starting_location = Shoreline(self)
        self.locations = {
            "Shoreline": self.starting_location,
            "Graveyard": Graveyard(self),
            "Shipwreck": Shipwreck(self), 
            "Castle": Castle(self), 
            "Mountain": Mountain(self)
        }


    def enter(self, ship):
        print("You're now on the island. Time to explore")
        

    def visit(self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class ArenaKeys(Item):
    keys = 1
    def __init__(self):
        super().__init__("Key", 100)  
        self.verb = "Unlock"  

class Shoreline(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Shoreline"
        self.verbs['west'] = self
        self.verbs['east'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['read'] = self
        self.keys = ArenaKeys()


    def enter(self):
        announce("You have landed on the Shoreline")
        announce("Just south of here is your shipwreck. You can also go east, west and south if you so dare.")
        announce("You have noticed a instructions on the ground, do you want to 'read' it?") 

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            if self.keys.keys > 0:
                announce("Using key to unlock the Castle")
                config.the_player.next_loc = self.main_location.locations["Castle"]
                self.keys.keys -= 1
            else:
                announce("Sorry you need to find an arena key to hang here")
        elif verb == "east":
            if self.keys.keys > 0:
                announce("Using key to unlock the Mountain")
                config.the_player.next_loc = self.main_location.locations["Mountain"]
                self.keys.keys -= 1
            else:
                announce("Sorry you need to find an arena key to hang here")
        elif verb == "west":
            if self.keys.keys > 0:
                announce("Using key to unlock the Graveyard")
                config.the_player.next_loc = self.main_location.locations["Graveyard"]
                self.keys.keys -= 1
            else:
                announce("Sorry you need to find an arena key to hang here")
        elif verb == "south":
            if self.keys.keys > 0:
                announce("Using key to unlock the Shipwreck")
                config.the_player.next_loc = self.main_location.locations["Shipwreck"]
                self.keys.keys -= 1
            else:
                announce("Sorry you need to find an arena key to hang here")
        elif verb == "read":
                announce("Welcome to Puzzle island, go through the puzzles in the Castle graveyard, shipwreck and mountains")
                announce("You will earn a key for each location you complete and those are needed to unlock other locations")
                announce("Here, you now have one key, use it to go where you want.")      
                announce("Why not 'fish' in the Shipwreck in the south to earn your first key?")           
     
class Graveyard(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Graveyard"



class Shipwreck(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Shipwreck"
        self.verbs['fish'] = self
        self.keys = ArenaKeys()

    def enter(self):
        announce("You are at the Shipwreck")
        announce("What's that? You notice some objects in the water. What would you like to do?")
        announce("Type 'fish' to start fishing.")
    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            config.the_player.next_loc = self.main_location.locations["Shoreline"]
        elif verb == "fish":
            self.events.append(FishGame())
            fishing_game = next((event for event in self.events if isinstance(event, FishGame)), None)
            if fishing_game:
                announce("You decide to try fishing...")
                announce("You can 'catch', or 'quit'. Keep trying until you find something")
                result = fishing_game.process({}) 
                announce(result["message"])

                if fishing_game.keys == 1:
                    config.the_player.add_to_inventory([self.keys])
                    announce("You found an ArenaKey")
                    ArenaKeys.keys += 1
                    
                self.events.remove(fishing_game)
                del fishing_game

class Mountain(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Mountain"
    def enter(self):
        announce("You are at the Shipwreck")
        announce("What's that? You notice some objects in the water. What would you like to do?")
        announce("Type 'fish' to start fishing.")
    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            config.the_player.next_loc = self.main_location.locations["Shoreline"]
        elif verb == "fish":
            self.events.append(FishGame())
            fishing_game = next((event for event in self.events if isinstance(event, FishGame)), None)
            if fishing_game:
                announce("You decide to try fishing...")
                announce("You can 'catch', or 'quit'. Keep trying until you find something")
                result = fishing_game.process({}) 
                announce(result["message"])

                if fishing_game.keys == 1:
                    config.the_player.add_to_inventory([self.keys])
                    announce("You found an ArenaKey")
                    ArenaKeys.keys += 1
                    
                self.events.remove(fishing_game)
                del fishing_game
class Castle(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Castle"
    def enter(self):
        announce("You are at the Shipwreck")
        announce("What's that? You notice some objects in the water. What would you like to do?")
        announce("Type 'fish' to start fishing.")
    def process_verb(self, verb, cmd_list, nouns):
        if verb == "north":
            config.the_player.next_loc = self.main_location.locations["Shoreline"]
        elif verb == "fish":
            self.events.append(FishGame())
            fishing_game = next((event for event in self.events if isinstance(event, FishGame)), None)
            if fishing_game:
                announce("You decide to try fishing...")
                announce("You can 'catch', or 'quit'. Keep trying until you find something")
                result = fishing_game.process({}) 
                announce(result["message"])

                if fishing_game.keys == 1:
                    config.the_player.add_to_inventory([self.keys])
                    announce("You found an ArenaKey")
                    ArenaKeys.keys += 1
                    
                self.events.remove(fishing_game)
                del fishing_game
