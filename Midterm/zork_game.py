import random

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        self.has_exit = False
        self.items = []
        self.dragon = False


class Game:
    def __init__(self):
        self.rooms = {
            "Green": Room("Green"),
            "Yellow": Room("Yellow"),
            "Red": Room("Red"),
            "Blue": Room("Blue"),
            "White": Room("White")
        }

        self.setup_map()

        self.current = self.rooms["Yellow"]
        self.has_key = False
        self.exit_unlocked = False

        self.boxes = {
            "Gold": None,
            "Silver": None
        }

        self.key_box = random.choice(["Gold", "Silver"])
        self.dragon_answered = False

        self.place_objects()

        self.riddle_question = "What has to be broken before you can use it?"
        self.riddle_answer = "egg"

    def setup_map(self):
        self.rooms["Yellow"].exits = {"north": "Blue", "south": "Red"}
        self.rooms["Red"].exits = {"north": "Yellow", "west": "Green"}
        self.rooms["Green"].exits = {"east": "Red", "south": "EXIT"}
        self.rooms["Green"].has_exit = True
        self.rooms["Blue"].exits = {"south": "Yellow", "west": "White"}
        self.rooms["White"].exits = {"east": "Blue"}

    def place_objects(self):
        room_names = list(self.rooms.keys())

        chosen_rooms = random.sample(room_names, 2)
        self.boxes["Gold"] = chosen_rooms[0]
        self.boxes["Silver"] = chosen_rooms[1]

        dragon_room = random.choice(room_names)
        self.rooms[dragon_room].dragon = True

    def describe_room(self):
        room = self.current
        print(f"\nYou are in the {room.name} room.")

        for direction, target in room.exits.items():
            if target == "EXIT":
                print(f"There is the EXIT to the {direction}.")
            else:
                print(f"There is a door to the {direction}.")

        for box, location in self.boxes.items():
            if location == room.name:
                print(f"There is a {box} box here.")

        if room.dragon:
            print("There is a dragon here.")

    def move(self, direction):
        if direction not in self.current.exits:
            print("You cannot go that way.")
            return

        target = self.current.exits[direction]

        if target == "EXIT":
            if self.exit_unlocked:
                print("Congratulations! You made it!")
                quit()
            else:
                print("The EXIT is locked.")
                return

        self.current = self.rooms[target]
        self.describe_room()

    def open_box(self):
        current_boxes = []

        for box, location in self.boxes.items():
            if location == self.current.name:
                current_boxes.append(box)

        if not current_boxes:
            print("There is no box here.")
            return

        chosen_box = current_boxes[0]

        print(f"{chosen_box} box is open.")

        if chosen_box == self.key_box:
            self.current.items.append("key")
        else:
            print("Wrong box! The other box locks permanently.")
            print("You lose!")
            quit()

    def get_key(self):
        if "key" in self.current.items:
            self.current.items.remove("key")
            self.has_key = True
            print("You now have the EXIT key.")
        else:
            print("There is no key here.")

    def unlock_exit(self):
        if not self.current.has_exit:
            print("There is no exit here.")
            return

        if self.has_key:
            self.exit_unlocked = True
            print("The EXIT is now unlocked.")
        else:
            print("You do not have the key.")

    def talk_to_dragon(self):
        if not self.current.dragon:
            print("There is no dragon here.")
            return

        if self.dragon_answered:
            print("The dragon refuses to answer again.")
            return

        print("Dragon asks:")
        print(self.riddle_question)

        answer = input("Answer: ").strip().lower()

        if answer == self.riddle_answer:
            print("Correct!")
            print(f"The key is in the {self.key_box} box.")
        else:
            print("Wrong answer. The dragon stays silent.")

        self.dragon_answered = True

    def play(self):
        print("Welcome to ZORK game!")
        self.describe_room()

        while True:
            command = input("\n> ").strip().lower()

            if command.startswith("go "):
                direction = command[3:]
                self.move(direction)

            elif command == "look":
                self.describe_room()

            elif command == "open box":
                self.open_box()

            elif command == "get key":
                self.get_key()

            elif command == "unlock exit":
                self.unlock_exit()

            elif command == "ask dragon":
                self.talk_to_dragon()

            elif command == "help":
                print("Commands:")
                print("go north / south / east / west")
                print("look")
                print("open box")
                print("get key")
                print("unlock exit")
                print("ask dragon")
                print("exit")

            elif command == "exit":
                if self.current.has_exit and self.exit_unlocked:
                    print("Congratulations! You made it!")
                    break
                else:
                    print("You cannot exit yet.")

            else:
                print("Unknown command.")


if __name__ == "__main__":
    game = Game()
    game.play()