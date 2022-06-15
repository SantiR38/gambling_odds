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
    def __init__(self, card1, card2, card3):
        self.card1: Card = card1
        self.card2: Card = card2
        self.card3: Card = card3

    def __repr__(self):
        return f"{self.card1}, {self.card2}, {self.card3}"

    @property
    def cards(self):
        return [self.card1, self.card2, self.card3]

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

    def get_envido_points(self):
        cards_suits = (card.suit for card in self.cards)
        cards_values = (card.value for card in self.cards)
        index_min = cards_values.index(min(cards_values))
        return sum(card.value_envido for card in self.cards)
