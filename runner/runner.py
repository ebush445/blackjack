import random

# deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A']

def draw_card(hand, drawn):
    card_index = random.randint(0, len(deck) - 1)
    while card_index in drawn:
        card_index = random.randint(0, len(deck) - 1)
    drawn.append(card_index)
    hand.append(deck[card_index])

def score(hand):
    total_score = 0
    aces = 0
    for card in hand:
        if card == 'A':
            total_score += 11
            aces += 1
        elif card in ['J', 'Q', 'K']:
            total_score += 10
        else:
            total_score += card

    # Adjust for aces if bust
    while total_score > 21 and aces > 0:
        total_score -= 10
        aces -= 1

    return total_score

# returns 1 if dealer won, -1 if player won, 0 if tie
def winner(player_hand, dealer_hand):
    dealer_score = score(dealer_hand)
    player_score = score(player_hand)

    if player_score > 21:
        return 1
    if dealer_score > 21:
        return -1
    if dealer_score > player_score:
        return 1
    if dealer_score < player_score:
        return -1
    return 0


def loop():
    print("--------------------------")
    print("New Game:")

    drawn_cards = []
    player_hand = []
    draw_card(player_hand, drawn_cards)
    draw_card(player_hand, drawn_cards)

    dealer_hand = []
    draw_card(dealer_hand, drawn_cards)
    draw_card(dealer_hand, drawn_cards)

    print(f"You: {player_hand} (score: {score(player_hand)})")
    print(f"Dealer: [{dealer_hand[0]}, ?]")

    # Player turn
    while score(player_hand) < 22:
        action = input("Hit or Stand? ").lower()
        if action == "hit":
            draw_card(player_hand, drawn_cards)
            print(f"You: {player_hand} (score: {score(player_hand)})")
        else:
            break

    # Dealer turn (hits until 17 or higher)
    while score(dealer_hand) < 17:
        draw_card(dealer_hand, drawn_cards)

    print(f"Dealer: {dealer_hand} (score: {score(dealer_hand)})")

    # Decide winner
    w = winner(player_hand, dealer_hand)
    if w == 1:
        if score(player_hand) > 21:
            print("Player Busts!")
        elif score(player_hand) == 21:
            print("Blackjack!")
        print("Dealer wins!")
    elif w == -1:
        if score(dealer_hand) > 21:
            print("Dealer Busts!")
        elif score(dealer_hand) == 21:
            print("Blackjack!")
        print("Player wins!")
    else:
        print("Tie!")


# Run game
while True:
    loop()







