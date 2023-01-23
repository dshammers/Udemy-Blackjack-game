import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
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
    
    def deal_hand(self,self.hand,deck):
        if len(self.hand) < 2:
            self.hand.append(deck.deal_one)

    def hit(self,new_card):
        self.hand.append(new_card)

    def display_hand(self):
        for i in self.hand:
            print i

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

    
class Player(Dealer):
    
    def __init_(self,bankroll):
        self.bankroll=bankroll
        self.bet_in_play=0
    
    def bet(self,bet):
        self.bankroll-=bet
        self.bet_in_play+=bet
    
    def winning(self,bet):
        self.bankroll+=bet*2

#functions

def dealer_hit(dealer):
    value=dealer.value_check
    if value > 17:
        dealer.hit
    else:
        return value

def win_check(player_value,dealer_value):
    if player_value > dealer_value:
        print ('Player wins!')
        player.winning
    elif dealer_value > player_value:
        print ('Dealer wins!')
        player.bet_in_play=0
    elif player_value == dealer_value:
        print ('Push!')
        player.bankroll+=player.bet_in_play

def player_choice(player):
    player.display_hand
    while True:
        choice=input('Would you like to hit or stay? ').lower()
        if choice=='hit':
            player.hit
            player.display_hand
        elif choice=='stay':
            break

def bust_check(hand):
    if hand.value > 21:
        print ('This hand is over 21!')
    else:
        print ('This hand can keep playing!')

#control logic

#dealer and player are made
dealer=Dealer()
player=Player(200)

#deck is made and shuffled
new_deck=Deck()
new_deck.shuffle

#game begins

while True:

    if player.bankroll==0:
        print ("You're out of money!")
        play_again=False
        break

    play_game=False

    choice=input('Would you like to play Blackjack? y/n: ').lower()
    if choice=='y':
        play_game=True
    if choice=='n':
        play_game=False
    
    while play_game:    
    #hands are dealt
    dealer.deal_hand
    player.deal_hand
    
    #player goes first
    player.display_hand
    dealer.display_hand

    player_choice(player)

    bust_check(player.hand)

    player.display_hand

    dealer_hit(dealer.hand)

    bust_check(dealer.hand)

    dealer.display_hand

    win_check(player.value_check,dealer.value_check)

    if play_again==False:
        break