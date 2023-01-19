import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,'Ace':11}

#classes
class Card():
    def __init__(self,rank,suit):
        self.suit=suit.capitalize()
        self.rank=rank.capitalize()
        self.value=values[rank.capitalize()]
        
    def __str__(self):
        return self.rank+' of '+self.suit
    
class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(rank,suit)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop[0]

class Dealer:

    def __init__(self):
        self.hand=[]
    
    def hit(self,new_card):
        self.hand.append(new_card)

    def display_hand(self):
        for i in self.hand:
            print i

    def aces(self):
        aces = 0
        for i in self.hand:
            if i.value == 11:
                aces += 1
        return aces

    def value_check(self):
        v = 0
        for i in self.hand:
            v += i.value
        if v > 21:
            for i in self.hand:
                if i.value == 11:
                    v-=10
                    if v <= 21:
                        return v
        return v

    def hit_or_stay(self):
        if self.value_check<17:
            self.hit

    
class Player(Dealer):
    
    def __init_(self,name,bankroll):
        self.name=name
        self.bankroll=bankroll
        self.bet_in_play=[]
    
    def bet(self,bet):
        self.bankroll-=bet
        self.bet_in_play+=bet

#functions        
def player_hit(num):
    