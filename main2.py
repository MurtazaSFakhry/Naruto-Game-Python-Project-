import random

print("Welcome!")
print("""   _  __              __         _____              
  / |/ /__ _______ __/ /____    / ___/__ ___ _  ___ 
 /    / _ `/ __/ // / __/ _ \  / (_ / _ `/  ' \/ -_)
/_/|_/\_,_/_/  \_,_/\__/\___/  \___/\_,_/_/_/_/\__/ 
""")

all_characters = {
    "Kiba Inuzuka": (55, 65),
    "Shino Aburame": (56, 66),
    "Kurenai Yuhi": (49, 59),
    "Ino Yamanaka": (50, 60),
    "Hinata Hyuga": (59, 69),
    "Asuma Sarutobi": (60, 70),
    "Zabuza Momochi": (69, 79),
    "Shikamaru Nara": (70, 80),
    "Sakura Haruno": (50, 60),
    "Neji Hyuga": (63, 73),
    "Hidan": (70, 80),
    "Sasori": (75, 85),
    "Kakuzu": (70, 80),
    "Konan": (72, 82),
    "Deidara": (72, 82),
    "Rock Lee": (74, 84),
    "Danzo Shimura": (69, 79),
    "Tsunade Senju": (80, 90),
    "Gaara": (81, 91),
    "A (Fourth Raikage)": (79, 89),
    "Killer B": (77, 87),
    "Kisame Hoshigaki": (77, 87),
    "Kabuto": (81, 91),
    "Orochimaru": (83, 93),
    "Jiraiya": (86, 96),
    "Hiruzen Sarutobi": (79, 89),
    "Kakashi Hatake": (86, 96),
    "Pain": (83, 93),
    "Nagato": (83, 93),
    "Tobirama Senju": (86, 96),
    "Itachi Uchiha": (87, 97),
    "Might Guy": (88, 98),
    "Minato Namikaze": (89, 99),
    "Obito Uchiha": (89, 99),
    "Sasuke Uchiha": (89, 99),
    "Hashirama Senju": (90, 100),
    "Madara Uchiha": (90, 100),
    "Naruto Uzumaki": (90, 100)
}

# Preventing people from typing numbers other than 1 AND preventing them from typing strings like "dog"
# or decimal numbers like 2.1!
while True:
    try:
        start_game = int(input("Type 1 to start the game: "))
    except ValueError:
        print("The game only functions when typing 1 - Please try again! ")
        continue
    if start_game != 1:
        print("The game only functions when typing 1 - Please try again! ")
    else:
        break

print()

# Generate options for player 1
player1_options = random.sample(list(all_characters.keys()), 10)

print("Player 1: Choose 3 characters from the following options:")
print("-" * 15)
for i, character in enumerate(player1_options, 1):
    print(f"{i}. {character}")
print()

# Player 1 selects characters
player1_choices = []
while len(player1_choices) < 3:
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice < 1 or choice > 10:
            raise ValueError
        character = player1_options[choice - 1]
        if character not in player1_choices:
            player1_choices.append(character)
        else:
            print("You have already chosen that character. Please select another.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")
    except IndexError:
        print("Invalid input! Please enter a number between 1 and 10.")

print()

# Generate options for player 2
player2_options = random.sample(list(all_characters.keys()), 10)

print("Player 2: Choose 3 characters from the following options:")
print("-" * 15)
for i, character in enumerate(player2_options, 1):
    print(f"{i}. {character}")
print()

# Player 2 selects characters
player2_choices = []
while len(player2_choices) < 3:
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice < 1 or choice > 10:
            raise ValueError
        character = player2_options[choice - 1]
        if character not in player2_choices:
            player2_choices.append(character)
        else:
            print("You have already chosen that character. Please select another.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")
    except IndexError:
        print("Invalid input! Please enter a number between 1 and 10.")

print()

print("Results:")
print("Player 1: Chosen characters")
print("-" * 15)
player1_score = 0
for character in player1_choices:
    score = random.randint(all_characters[character][0], all_characters[character][1])
    player1_score += score
    print(f"{character}: {score}")


print()

print("Player 2: Chosen characters")
print("-" * 15)
player2_score = 0
for character in player2_choices:
    score = random.randint(all_characters[character][0], all_characters[character][1])
    player2_score += score
    print(f"{character}: {score}")

print()

if player1_score > player2_score:
    print("Player 1 wins!")
elif player1_score < player2_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")
