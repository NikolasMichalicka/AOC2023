import time
from operator import itemgetter

start_time = time.perf_counter()
file = open("input.txt", "r")
lines = file.readlines()

'''
1  Five of a kind, where all five cards have the same label: AAAAA
2  Four of a kind, where four cards have the same label and one card has a different label: AA8AA
2  Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
3  Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
3  Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
4  One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
5  High card, where all cards' labels are distinct: 23456
   700 00 00 00 00 00
'''

cards_value = ["J","2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def val(card):
    return f'{cards_value.index(card):02d}'

def cards(line):
    deck, bid = line.split()
    bid = int(bid)

    value = ''
    for card in deck:
        value += val(card)

    cards = []
    joker = 0
    while deck != '':
        card = deck[0]
        if card == 'J':
            joker = deck.count(card)
        else:
            cards.append([cards_value.index(card),deck.count(card)])
        deck = deck.replace(card, '')
    cards = sorted(cards, key=itemgetter(1), reverse=True)

    match len(cards):
        case 0:
            return [int('7'+value),bid]
        case 1:
            return [int('7'+value),bid]
        case 2:
            if cards[0][1]+joker == 4:
                return[int('6'+value),bid]
            return [int('5'+value),bid]
        case 3:
            if cards[0][1]+joker == 3:
                return [int('4'+value),bid]
            return [int('3'+value),bid]

        case 4:
            return [int('2'+value),bid]
        case default:
            return [int('1'+value),bid]


parts = []
for line in lines:
    print(line, end='')   
    parts.append(cards(line))

parts = sorted(parts, key=itemgetter(0))
print(parts)
ans = 0
for i in range(len(parts)):
    ans+=parts[i][1]*(i+1)
print(ans)

print(f"Part2 done in {(time.perf_counter()-start_time):02f} seconds")
