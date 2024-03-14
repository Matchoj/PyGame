from Cards import  playersee, player2 , Sort
import os


title1 = 'PLAYER ONE CARDS: \n'
title2 = 'PLAYER TWO HAVE CARDS :'
title3 = 'IN PAIL IS :'
Line = '='* 130
pail = []


def display1(player2, pail):
    nrP2 = str(len(player2))
    nrPail = str(len(pail))
    if len(pail) > 0:
        a = pail[-1:]
        a1=a[0]
        b = a1['F']
        c = a1['C']
        txt = "Top card : %s %s" % (b, c)
    else:
        txt = "No cards in Pail"

    print(Line.center(130))
    print(title2.center(130))
    print(nrP2.center(130))
    print('\n')
    print(title3.center(130))
    print(nrPail.center(130), "\n", txt.center(100).upper())
    print('\n')
    print(title1.center(130))

    return





def display2(arg):
    SV = arg.copy()
    while len(arg) > 0:
        player = arg.copy()
        line = []
        line1 = ''
        none = '%20s\t' % (line1)
        d = 0
        for cd in player:
            if cd['P'] == d:
                copy_cd = cd.copy()
                x = copy_cd['F']
                y = copy_cd['C']
                card1 = "{} {}".format(x, y)
                card11 = "%20s\t" % (card1)
                line.append(card1)
                line1 += card11
                arg.remove(cd)
                d += 1

            elif cd['P'] < d:
                continue

            elif cd['P'] - d==0:
                line.append(none)
                line1 += none

            elif cd['P'] > d:
                blank = cd['P'] - d
                for i in range(blank):
                    line.append(none)
                    line1 += none
                copy_cd = cd.copy()
                x = copy_cd['F']
                y = copy_cd['C']
                card1 = "{} {}".format(x, y)
                card11= "%20s\t" % (card1)
                line1 += card11
                line.append(card1)
                arg.remove(cd)
                d = cd['P']
                d += 1

        if len(line) < 6:
            blank = 6 - len(line)
            for i in range(blank):
                line.append(none)
                line1 += none

        print(line1)
    return SV




def Last(arg):
    z=arg[-1:]
    z1=z[0]
    return z1


player1 =playersee.copy()
def gra():
    warunek = True
    choose = input('\nChoose POWER of card you want to place(from 0 to 5 where: 0 is NINE and 5 is ACE), or choose "p" to pull card from card Pali:  ')

    while warunek:
        copy_pail = pail.copy()
        if choose == 'p':
            if len(copy_pail) == 0:
                choose = input("There's nothing to pull from pail! its empty! choose another option:  ")
            else :
                x = Last(pail)
                player1.append(x)
                pail.remove(x)
                warunek = False
        elif choose.isdigit() and int(choose) in range(0, 6):
            for card in player1:
                if card['P'] == int(choose):
                    if len(pail) == 0:
                        pail.append(card)
                        player1.remove(card)
                        warunek = False
                        break
                    else:
                        x=Last(pail)
                        if x['P'] <= int(choose):
                            pail.append(card)
                            player1.remove(card)
                            warunek = False
                            break
            if len(pail) == len(copy_pail):
                choose = input('Wrong option try again or press "p" to pull cards rom Pail:')
            else:
                warunek = False
        else:
            choose = input('choose wrong option please try again:')\

    if len(pail) > 0:
        x=Last(pail)
        topCard = x['P']
    else:
        topCard = 0

    warunek = True
    while warunek:  # Player2( computer) round
        copy_pail = pail.copy()
        for card in player2:
            if card['P'] == topCard:
                pail.append(card)
                player2.remove(card)
                warunek = False
                break
        if len(pail) > len(copy_pail):
            warunek = False
        elif len(pail) == len(copy_pail):
            for card in player2:
                if card['P'] > topCard:
                    pail.append(card)
                    player2.remove(card)
                    warunek = False
                    break
            if len(pail) == len(copy_pail):
                if len(pail) > 1:
                    x=Last(pail)
                    player2.append(x)
                    pail.remove(x)
                    warunek = False
                else:
                    warunek = False


while len(player1) > 0 or len(player2) > 0:
    os.system('cls')
    display1(player2, pail)
    player1 = display2(player1)
    gra()
    playersee.clear()
    playersee =Sort(player1)
    player1 = playersee
    if len(player1) == 0:
        print("\nEND GAME ! PLAYER 1 WINS !!!".center(100))
        break
    elif len(player2) == 0:
        print("\nEND GAME! PALYER 2 WINS !!!".center(100))
        break



