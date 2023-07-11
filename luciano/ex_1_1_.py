import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
"""
collections.namedtuple - используется для построения классов, 
содержащих только атрибуты и никаких методов!

В примере выше, переменная Card является полноценным классом,
экземпляры Card будут отображать наши карты.
"""


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # Здесь последовательность рангов карт
    suits = 'spades diamonds clubs hearts'.split()  # Тип карт

    def __init__(self):
        """
        При создании экземпляра FrenchDeck
        будет сгенерирована колода из 52 карт.
        """
        # self._cards = [Card(rank, suit)
        #                for suit in self.suits
        #                for rank in self.ranks]

        self._cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(rank, suit))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


"""
Класс FrenchDeck подобно полноценной последовательностью,
имеет интерфейсы getitem и len.
"""
deck = FrenchDeck()
# print(choice(deck))  # Рандомный выбор карты из колоды

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

lst_res = []
lst_rank_value = []
lst_suit_values_card = []

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)

    res = rank_value * len(suit_values) + suit_values[card.suit]
    lst_rank_value.append(rank_value)
    lst_res.append(res)
    lst_suit_values_card.append(suit_values[card.suit])
    return res


for card in sorted(deck, key=spades_high):
    print(card)

print(lst_res)
print(*lst_rank_value)
print(*lst_suit_values_card)
