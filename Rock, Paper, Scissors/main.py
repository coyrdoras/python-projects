import random
from time import sleep

class Gamer():
    def __init__(self, secim, score):
        self.secim = secim
        self.score = score

def start():
    print("""
    Welcome to the game!
    The game started!
""")
    
start()
print("Options:\n1. Rock\n2. Paper\n3. Scissors\n")

a = random.choice(["1", "2", "3"])

program = Gamer(secim = a, score = 0)
player = Gamer(secim = input("Choose a option: "), score = 0)

if player.secim not in ["1", "2", "3"]:
    print("\nTypeError: Please choose a suitable option!\n")
    player.secim = input("Choose a option: ")
else:
    print(f"\nProgram's choice was {a}\n")

def lose():
    program.score += 1
    return program.score

def win():
    player.score += 1
    return player.score

def draw():
    if player.secim == program.secim:
        print("Draw!\n")

def sec():   
    while int(player.score) < 3 and int(program.score) < 3:
        if player.secim not in ["1", "2", "3"]:
            print("\nTypeError: Please choose a suitable option!\n")
            player.secim = input("Choose a option: ")

            continue
        else:
            if player.secim == "1" and program.secim == "2":
                lose()
            elif player.secim == "1" and program.secim == "3":
                win()
            elif player.secim == "2" and program.secim == "1":
                win()
            elif player.secim == "2" and program.secim == "3":
                lose()
            elif player.secim == "3" and program.secim == "1":
                lose()
            elif player.secim == "3" and program.secim == "2":
                win()
            else:
                draw()
        if player.score == 3 or program.score == 3:
            if player.score == 3:
                print("You won!")
            else:
                print("You lost!")
            break
        player.secim = input("Choose a option: ")
        program.secim = random.choice(["1", "2", "3"])
        print(f"\nProgram's choice was {program.secim}\n")
    
    return player.score, program.score
    
sec()

print(f"\nPlayer's score was {player.score}")
print(f"Program's score was {program.score}")