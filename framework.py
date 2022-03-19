from black_jack_arts import logo
import random
print(logo)
# These are the available cards from which 2 cards for user is selected and 2 cards for computer is selected
user_cards = []
computer_cards = []
is_game_finished = False
user_restart = 'y'

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card




def calculate_score(card_list):
    """This function takes card list and calculates the sum of the cards"""
    if 11 in card_list and 10 in card_list and len(card_list) == 2:
        return 0
    if 11 in card_list:
        if sum(card_list) > 21:
            card_list.remove(11)
            card_list.append(1)
    return sum(card_list)


def compare(us_score, comp_score):
    if us_score > 21:
        return "SORRY ! you lost"
    elif comp_score > 21:
        return "HURRAY !! You won"
    elif us_score == comp_score:
        return "Match Drawn"
    elif us_score == 0:
        return "HURRAY !! Blackjack"
    elif comp_score == 0:
        return "Sorry !! Computer has got blackjack"
    elif us_score > comp_score:
        return "HURRAY !!You won"
    elif us_score < comp_score:
        return "Sorry !! You lost"


while user_restart == 'y':

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_finished:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards {user_cards}, score {user_score}")
        print(f"Computer's first card {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_finished = True
        else:
            user_prompt = input("Do you want to take another card ? 'y' or 'n' ").lower()
            if user_prompt == 'y':
                user_cards.append(deal_card())
            else:
                is_game_finished = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"final cards {user_cards} with score {user_score}")
    print(f"final card of Computer {computer_cards} with score {computer_score}")
    print(compare(user_score, computer_score))
    user_restart = input("Do you want to restart the game 'y' or 'n' ").lower()

