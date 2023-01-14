from collections import Counter
from pathlib import Path

data_folder = Path("euler/inputs/")
file_to_open = data_folder / "p054_poker.txt"
with open(file_to_open) as f: input = f.read()

hands = input.splitlines()

class card():
    def __init__(self, c):
        self.value = c[0]
        self.suit = c[1]
        self.value_int = self.value_int()
        self.suit_int = self.suit_int()

    def value_int(self):
        if self.value == 'T':
            return 10
        elif self.value == 'J':
            return 11
        elif self.value == 'Q':
            return 12
        elif self.value == 'K':
            return 13
        elif self.value == 'A':
            return 14
        else:
            return int(self.value)

    def suit_int(self):
        if self.suit == 'H':
            return 1
        elif self.suit == 'D':
            return 2
        elif self.suit == 'C':
            return 3
        elif self.suit == 'S':
            return 4

    def __repr__(self):
        return f'{self.value}{self.suit}'

class hand():
    def __init__(self, cards):
        self.cards = cards
        self.values = [c.value_int for c in cards]
        self.suits = [c.suit_int for c in cards]
        self.values.sort()
        self.suits.sort()
        self.value_counts = self.value_counts()
        self.is_straight = self.is_straight()
        self.is_flush = self.is_flush()
        self.is_straight_flush = self.is_straight_flush()
        self.is_royal_flush = self.is_royal_flush()
        self.is_four_of_a_kind = self.is_four_of_a_kind()
        self.is_full_house = self.is_full_house()
        self.is_three_of_a_kind = self.is_three_of_a_kind()
        self.is_two_pair = self.is_two_pair()
        self.is_one_pair = self.is_one_pair()
        self.high_card = max(self.values)

    def __repr__(self):
        return f'{self.cards}'

    def value_counts(self):
        return Counter(self.values)

    def is_straight(self):
        if self.values == [2,3,4,5,14]:
            return True
        for i in range(4):
            if self.values[i+1] - self.values[i] != 1:
                return False
        return True

    def is_flush(self):
        for i in range(4):
            if self.suits[i+1] != self.suits[i]:
                return False
        return True

    def is_straight_flush(self):
        return self.is_straight and self.is_flush

    def is_royal_flush(self):
        return self.is_straight_flush and self.values == [10,11,12,13,14]

    def is_four_of_a_kind(self):
        if sorted(self.value_counts.values()) == [1,4]:
            self.quad = [k for k in self.value_counts if self.value_counts[k] == 4][0]
            return True

    def is_full_house(self):
        if sorted(self.value_counts.values()) == [2,3]:
            self.trips = [k for k in self.value_counts if self.value_counts[k] == 3][0]
            self.pair = [k for k in self.value_counts if self.value_counts[k] == 2][0]
            return True

    def is_three_of_a_kind(self):
        if sorted(self.value_counts.values()) == [1,1,3]:
            self.trips = [k for k in self.value_counts if self.value_counts[k] == 3][0]
            return True

    def is_two_pair(self):
        if sorted(self.value_counts.values()) == [1,2,2]:
            pair1 = [k for k in self.value_counts if self.value_counts[k] == 2][0]
            pair2 = [k for k in self.value_counts if self.value_counts[k] == 2][1]
            self.pair1, self.pair2 = sorted([pair1, pair2], reverse=True)
            self.solo = [k for k in self.value_counts if self.value_counts[k] == 1][0]
            return True

    def is_one_pair(self):
        if sorted(self.value_counts.values()) == [1,1,1,2]:
            self.pair = [k for k in self.value_counts if self.value_counts[k] == 2][0]
            return True

ws = 0
for h in hands:
    h = [card(c) for c in h.split()]
    p1 = hand(h[:5])
    p2 = hand(h[5:])
    if p1.is_royal_flush:
        if p2.is_royal_flush:
            continue
        ws += 1
        continue
    if p1.is_straight_flush:
        if p2.is_straight_flush and p2.high_card >= p1.high_card:
            continue
        ws += 1
        continue
    if p1.is_four_of_a_kind:
        if p2.is_straight_flush:
            continue
        if p2.is_four_of_a_kind and p2.quad >= p1.quad:
            continue
        ws += 1
        continue
    if p1.is_full_house:
        if p2.is_straight_flush or p2.is_four_of_a_kind:
            continue
        if p2.is_full_house:
            if p2.trips > p1.trips:
                continue
        ws += 1
        continue
    if p1.is_flush:
        if p2.is_straight_flush or p2.is_four_of_a_kind or p2.is_full_house:
            continue
        if p2.is_flush:
            p1w = False
            for a,b in zip(sorted(p1.values, reverse=True), sorted(p2.values, reverse=True)):
                if a > b:
                    p1w = True
                    break
                elif a < b:
                    break
            if p1w:
                ws += 1
            continue
        ws += 1
        continue
    if p1.is_straight:
        if p2.is_flush or p2.is_four_of_a_kind or p2.is_full_house:
            continue
        if p2.is_straight and p2.high_card >= p1.high_card:
            continue
        ws += 1
        continue
    if p1.is_three_of_a_kind:
        if p2.is_flush or p2.is_four_of_a_kind or p2.is_full_house or p2.is_straight:
            continue
        if p2.is_three_of_a_kind:
            if p2.trips > p1.trips:
                continue
        ws += 1
        continue
    if p1.is_two_pair:
        if p2.is_flush or p2.is_four_of_a_kind or p2.is_full_house or p2.is_straight or p2.is_three_of_a_kind:
            continue
        if p2.is_two_pair:
            if p2.pair1 > p1.pair1:
                continue
            if p2.pair1 == p1.pair1:
                if p2.pair2 > p1.pair2:
                    continue
                if p2.pair2 == p1.pair2:
                    if p2.solo >= p1.solo:
                        continue
        ws += 1
        continue
    if p1.is_one_pair:
        if p2.is_flush or p2.is_four_of_a_kind or p2.is_full_house or p2.is_straight or p2.is_three_of_a_kind or p2.is_two_pair:
            continue
        if p2.is_one_pair:
            if p2.pair > p1.pair:
                continue
            if p2.pair == p1.pair:
                p1w = False
                p1_leftovers = [v for v in p1.values if v != p1.pair]
                p2_leftovers = [v for v in p2.values if v != p2.pair]
                for a,b in zip(sorted(p1_leftovers, reverse=True), sorted(p2_leftovers, reverse=True)):
                    if a > b:
                        p1w = True
                        break
                    elif a < b:
                        break
                if p1w:
                    ws += 1
                continue
        ws += 1
        continue
    if p2.is_flush or p2.is_four_of_a_kind or p2.is_full_house or p2.is_straight or p2.is_three_of_a_kind or p2.is_two_pair or p2.is_one_pair:
        continue
    p1w = False
    for a,b in zip(sorted(p1.values, reverse=True), sorted(p2.values, reverse=True)):
        if a > b:
            p1w = True
            break
        elif a < b:
            break
    if p1w:
        ws += 1

print(ws)
