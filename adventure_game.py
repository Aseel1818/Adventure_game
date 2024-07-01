import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def player_choices(enemy, player):
    print_pause("Enter 1 to knock the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    player_choice = ''
    while True:
        player_choice = input("Please enter your choice (1, 2)\n")
        if player_choice in ['1', '2']:
            break
    if (player_choice == '1'):
        house(enemy, player)
    elif (player_choice == '2'):
        cave(enemy, player)


def start_messages(enemy):
    print_pause(
        "You find yourself standing in an open field,"
        "filled with grass and yellow wildflowers.")
    print_pause(
        f"Rumoar has is that a {enemy['name']} is somewhere around here,"
        "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("In your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effictive) dagger.")


def play_again(enemy, player):
    choice = ''
    while True:
        choice = input(
            "Would you like to play again? (y/n).\n")
        if choice.lower() in ["y", "n"]:
            break
    if (choice.lower() == "y"):
        if not (player_health(player, enemy)):
            start_messages(enemy)
            player_choices(enemy, player)
    elif (choice.lower() == "n"):
        print("Game Over\n")


def player_health(player, enemy):
    if player['health'] <= 0 and enemy['health'] <= 0:
        return True


def player_health_printer(player, enemy):
    if player['health'] <= 0:
        print("You have been defeated. Game over!")
    elif enemy['health'] <= 0:
        print("You have defeated the enemy. Congratulations!")


def game_over(enemy, player):
    print("Game Over. Thanks for playing")
    play_again(enemy, player)


def fight(enemy, player):

    player_health_printer(player, enemy)
    while not player_health(player, enemy):
        print(f"Player {player['name']} you're fighting a {enemy['name']}.")
        player_strike = random.randint(1, player["strength"])
        enemy_strike = random.randint(1, enemy["strength"])
        print_pause(
            f"Using your {player['weapon']} you land a blow on"
            f" the {enemy['name']} and inflict {player_strike} damage")
        enemy['health'] -= player_strike
        if (enemy['health'] <= 0):
            print_pause(f"Victory! The {enemy['name']} has been vanquished!")
            print_pause("Well Done!, you've won the game!")
            game_over(enemy, player)
            break

        print_pause(
            f"The {enemy['name']} hits back ,causing {enemy_strike} damage.")
        player["health"] -= enemy_strike
        if (player['health'] <= 0):
            print_pause("Game over. You lost the battle.")
            game_over(enemy, player)
            break


def encounter_monster(enemy, player):
    encounter_likelihood = random.random()
    if encounter_likelihood < 0.5:
        print_pause(
            "********** You got a chance to "
            "encount the monster **********")
        combat(enemy, player)
    else:
        print_pause(
            "You explore further but find no creatures or "
            "challenges.The adventure ends here.")
        game_over(enemy, player)


def field(enemy, player):
    print_pause("You walk back out to the field.")
    player_choices(enemy, player)


def cave(enemy, player):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger"
                "and take the sword with you.")
    print_pause("You walk back out to the field.")
    encounter_monster(enemy, player)


def house(enemy, player):
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door"
        f"opens and out steps a {enemy['name']}.")
    print_pause(f"Eep! This is the {enemy['name']}'s house!")
    combat(enemy, player)


def combat(enemy, player):
    print_pause(f"{enemy['name']} strikes at you!")
    while True:
        choice = input("Choose 1 for fight Or 2 run away.\n")
        if choice in ['1', '2']:
            break
    if (choice == '1'):
        fight(enemy, player)

    elif (choice == '2'):
        print_pause(
            "You retrate to the field."
            " Thankfully you don't seem to have been followed.")
        field(enemy, player)


def main():

    player_health = random.randint(10, 100)
    player_name = input("Dear player please enter your name \n")
    player = {"weapon": "dagger", "health": player_health,
              "level": 2, "armor": 5, "strength": 10, "name": player_name}

    enemies = [
        {"level": 3, "armor": 2, "strength": 7,
         "health": 100, "name": "Pirate"},
        {"level": 2, "armor": 4, "strength": 6,
         "health": 50, "name": "Gorgon"},
        {"level": 4, "armor": 3, "strength": 7,
         "health": 60, "name": "Dragon"},
        {"level": 2, "armor": 1, "strength": 8,
            "health": 50, "name": "Wicked fairie"},
        {"level": 1, "armor": 3, "strength": 9, "health": 100,
         "name": "Troll"}]

    creature = random.choice(enemies)
    start_messages(creature)
    print_pause(
        f"You come across a {creature['name']}"
        f"with {creature['health']} health.")
    player_choices(creature, player)


if __name__ == "__main__":
    main()
