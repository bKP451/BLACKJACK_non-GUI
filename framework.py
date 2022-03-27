# Hint 4 : Create a deal_card() function that uses the List below to **return
# a random card
from black_Jack_arts import logo
import random
import os
user_restart = 'y'


def clear_screen():
    os.system('clear')


def deal_card():
    """Returns a card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    """Calculates score from the card list."""
    # Returns 0 for blackjack
    if len(card_list) == 2 and (11 in card_list and 10 in card_list):
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        # Replace 11 with 1
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_total, computer_total):
    if user_total > 21:
        return "You lose."
    elif computer_total > 21:
        return "Hurray !! You win"
    elif user_total == computer_total:
        return "Match drawn"
    elif user_total == 0:
        return "Hurray !!! You win."
    elif computer_total == 0:
        return "You lose"
    elif user_total > computer_total:
        return "Hurray !!! You win."
    else:
        return "Sorry you lose."


while user_restart == 'y':
    user_card = []
    computer_card = []
    game_end = False
    for i in range(0, 2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_end:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        clear_screen()
        print(logo)
        print(f"Your cards are {user_card} SCORE :{user_score}")
        print(f"Dealer_card is [{computer_card[0]},unknown]")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            user_prompt = input("Do you want to draw another card ? Y/N  ").lower()
            if user_prompt == 'y':
                user_card.append(deal_card())
            else:
                # TODO Let computer draw cards until the score is less than 17
                game_end = True

    while computer_score != 0 and user_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"The dealer cards were {computer_card} Score: [{computer_score}].")
    print(compare(user_total=user_score, computer_total=computer_score))
    user_restart = input("Do you want to  restart Blackjack ? Y/N ").lower()

