import random


class Card:
    suits_options = ["espada", "copa", "oro", "basto"]
    value_options = ["as", "dos", "tres", "cuatro", "cinco", "seis", "siete", "sota", "caballo", "rey"]
    envido_dict = {
        "as": 1,
        "dos": 2,
        "tres": 3,
        "cuatro": 4,
        "cinco": 5,
        "seis": 6,
        "siete": 7,
        "sota": 0,
        "caballo": 0,
        "rey": 0
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value.capitalize() + " de " + self.suit

    @property
    def value_envido(self):
        return self.envido_dict[self.value]

    def __add__(self, other):
        return self.value_envido + other.value_envido

    @classmethod
    def generate_random_card(cls):
        suit = random.choice(cls.suits_options)
        value = random.choice(cls.value_options)
        return cls(suit, value)


class Hand:
    __cards = None
    __cards_suits = None

    def __init__(self, card1, card2, card3):
        self.card1: Card = card1
        self.card2: Card = card2
        self.card3: Card = card3

    def __repr__(self):
        return f"{self.card1}, {self.card2}, {self.card3}"

    @property
    def cards(self):
        return self.__cards or [self.card1, self.card2, self.card3]

    @property
    def cards_suits(self):
        return self.__cards_suits or [card.suit for card in self.cards]

    @classmethod
    def generate_random_hand(cls):
        card1 = Card.generate_random_card()
        difference = lambda x, y: x.suit != y.suit or x.value != y.value
        while True: # Generate unique second card
            card2 = Card.generate_random_card()
            if difference(card1, card2):
                break
        while True: # Generate unique third card
            card3 = Card.generate_random_card()
            if difference(card1, card3) and difference(card2, card3):
                break

        return cls(card1, card2, card3)

    @property
    def max_card_value(self):
        return max(card.value_envido for card in self.cards)

    def get_envido_points(self):
        cards_values = [card.value_envido for card in self.cards]

        equal_values = len(set(self.cards_suits))

        # All same suit
        if equal_values == 1:
            cards_values.remove(min(cards_values))
            return sum(cards_values) + 20

        # Two same suit
        elif equal_values == 2:
            repeated_suit = max(set(self.cards_suits),
                key = self.cards_suits.count)
            envido_points = sum([
                x.value_envido for x in self.cards \
                    if x.suit == repeated_suit
            ]) + 20
            return envido_points

        # All different suits
        return self.max_card_value