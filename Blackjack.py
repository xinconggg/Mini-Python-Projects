############### Our Blackjack House Rules #####################

## The deck is unlimited in size.  
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random

def play_blackjack():
    player_hand = []
    computer_hand = []

    # Deal 2 initial cards to player and computer
    for i in range(2):
        player_hand = deal_card(player_hand)
        computer_hand = deal_card(computer_hand)
    
    # Show Player's hand and Computer's first card
    print(f"Your hand is: {player_hand}, Your sum is: {calculate_value(player_hand)}")
    print(f"Computer's first card is: {computer_hand[0]}")

    # Check for Blackjack
    if check_blackjack(computer_hand):
        print("************************************************************************************************************")
        print("BLACKJACK!!! Computer Wins!")
        print(f"Your cards: {player_hand}, Your sum: {calculate_value(player_hand)}")
        print(f"Computer's cards: {computer_hand}, Your sum: {calculate_value(computer_hand)}")
        
    if check_blackjack(player_hand):
        print("************************************************************************************************************")
        print("BLACKJACK!!! Player Wins!")
        print(f"Your cards: {player_hand}, Your sum: {calculate_value(player_hand)}")
        print(f"Computer's cards: {computer_hand}, Your sum: {calculate_value(computer_hand)}")
        
    
    # Continue / End game
    game_over = False
    while not game_over:
        draw_card = input("Do you wish to draw a card? Y or N? ").upper()
        if draw_card == "Y":
            player_hand = deal_card(player_hand)
            print(f"Your hand is: {player_hand}, Your sum is: {calculate_value(player_hand)}")
            if check_burst(player_hand):
                print("You Burst! Game Over!")
                game_over = True
        
        elif draw_card == "N":
            if calculate_value(player_hand) < 17:
                print("Your hand value is less than 17, You have to draw.")
            else:
                game_over = True

        else: 
            print("Invalid input! Please enter either Y or N.")
    
    # Computer's Turn
    while calculate_value(computer_hand) <= 16:
        computer_hand = deal_card(computer_hand)
        if check_burst(computer_hand):
                print("Computer Burst! You Win!")
                game_over = True
    
    # Show final hand value of both Player & Computer and Determine thw winner
    print("************************************************************************************************************")
    print(f"Your cards: {player_hand}, Your sum: {calculate_value(player_hand)}")
    print(f"Computer's cards: {computer_hand}, Your sum: {calculate_value(computer_hand)}")
    print(check_winner(player_hand, computer_hand))

    # Check if want to play again
    play_again = input("Do you wish to play again? Y or N? ").upper()
    if play_again == "Y":
        play_blackjack()
    else:
        print("Thanks for playing!")


def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))
    return hand

def calculate_value(hand):
    value = sum(hand)

    # Change value of ace from "11" to "1" if value of hand is over "21"
    if sum(hand) > 21:
        ace_count = hand.count(11)
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
    return value

def check_blackjack(hand):
    if sum(hand) == 21:
        return True

def check_burst(hand):
    if sum(hand) > 21:
        return True

def check_winner(player_hand, computer_hand):
    if (21 - calculate_value(player_hand)) < (21 - calculate_value(computer_hand)):
        return "Player wins!"
    elif (21 - calculate_value(player_hand)) > (21 - calculate_value(computer_hand)):
        return "Computer wins!"
    else:
        return "It's a draw!"

play_blackjack()


