import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

blackjack_hand = {
    "player": [],
    "computer": [],
}

def calculate_player_cards(value):
    player_score=sum(value)
    return player_score

def calculate_computer_cards(value):
    computer_score=sum(value)
    return computer_score


def computer_ace(value):
    computer_score=calculate_computer_cards(value)
    if computer_score > 21:
        for i in range(len(value)):
            if value[i]==11:
                value[i]=1

def verify_player_ace(value):
    player_score=calculate_player_cards(value)
    if player_score > 21:
        for i in range(len(value)):
            if value[i]==11:
                value[i]=1

def get_computer_cards(computer, player):
    computer_score=calculate_computer_cards(computer)
    while computer_score < 16:
        blackjack_hand["computer"].append(random.choice(cards))
        computer_ace(blackjack_hand["computer"])
        computer_score = calculate_computer_cards(computer)

def blackjack(start_game):
    if start_game=='y':
        print(logo)
        blackjack_hand["player"]=[random.choice(cards), random.choice(cards)]
        blackjack_hand["computer"]=[random.choice(cards)]
        print(f"Your cards: {blackjack_hand["player"]}, current score: {calculate_player_cards(blackjack_hand["player"])}")
        print(f"Computer's first card: {blackjack_hand["computer"]}")
        get_player_card=input("Type 'y' to get another card, type 'n' to pass: ")
        while get_player_card == "y":
            blackjack_hand["player"].append(random.choice(cards))
            verify_player_ace(blackjack_hand["player"])
            print(f"Your cards: {blackjack_hand["player"]}, current score: {calculate_player_cards(blackjack_hand["player"])}")
            print(f"Computer's first card: {blackjack_hand["computer"]}")
            if calculate_player_cards(blackjack_hand["player"]) > 21:
                print(f"Your final hand: {blackjack_hand["player"]}, final score: {calculate_player_cards(blackjack_hand["player"])}")
                print(f"Computer's final hand: {blackjack_hand["computer"]}, final score: {calculate_computer_cards(blackjack_hand["computer"])}")
                print("You went over. You lose :(")
                restart_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                if restart_game=='y':
                    print("\n" * 20)
                    blackjack(restart_game)
                else:
                    return 0
            get_player_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_player_card == "n":
            print(f"Your final hand: {blackjack_hand["player"]}, final score: {calculate_player_cards(blackjack_hand["player"])}")
            get_computer_cards(blackjack_hand["computer"], blackjack_hand["player"])
            print(f"Computer's final hand: {blackjack_hand["computer"]}, final score: {calculate_computer_cards(blackjack_hand["computer"])}")
            if calculate_computer_cards(blackjack_hand["computer"]) > 21:
                print(f"Opponent went over. You win :)")
            elif calculate_player_cards(blackjack_hand["player"]) < calculate_computer_cards(blackjack_hand["computer"]):
                print("You lose :(")
            elif calculate_player_cards(blackjack_hand["player"]) == calculate_computer_cards(blackjack_hand["computer"]):
                print("Draw")
            elif calculate_player_cards(blackjack_hand["player"]) == 21 and calculate_player_cards(blackjack_hand["player"]) > calculate_computer_cards(blackjack_hand["computer"]):
                print("Win with a Blackjack")
            elif calculate_computer_cards(blackjack_hand["computer"]) == 21 and calculate_computer_cards(blackjack_hand["computer"]) > calculate_player_cards(blackjack_hand["player"]):
                print("Lose, opponent has Blackjack")
            else:
                print("You win")
            restart_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if restart_game == 'y':
                print("\n" * 20)
                blackjack(restart_game)
            else:
                return 0
    else:
        return 0

start_game= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
blackjack(start_game)
