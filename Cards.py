import random

def Cards():
    figures = [
        {'P': 5, 'F': 'Ace'},
        {'P': 4, 'F': 'King'},
        {'P': 3, 'F': 'Queen'},
        {'P': 2, 'F': 'Jack'},
        {'P': 1, 'F': 'Ten'},
        {'P': 0, 'F': 'Nine'}]
    colors = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


    cards = []


    # Preparing  play cards
    for c in colors:
        for f in figures:
            x = f.copy()
            x['C'] = c
            cards.append(x)


    random.shuffle(cards)

    return cards


cards = Cards()

pail = []
player1 = []
player2 = []
playersee = []

while len(cards) > 0:
    player1.append(cards.pop())
    player2.append(cards.pop())

def Sort(arg):
    z = 0
    while len(arg) > 0:
        player = arg.copy()
        for card in player:
            if card['P'] == z:
                card_copy = card.copy()
                playersee.append(card_copy)
                arg.remove(card)
        z += 1
        if z == 6:
            z = 0

    return playersee

playersee = Sort(player1)


