import random
import sys
'''

Blacjack rules
A are 1 or 10s
2-10 are normal points
J, Q, K are 10s
Over 21 is bust and dealer stands on 17 or more
On 21 without any draws is a win unless the dealer also has 21
Player gets 2 cards first and choose a action to stand or take a card

1. Skapa lista med vad det finns i kortlek och skapa en random 
där spelaren får 2 kort och sedan 1 kort för dealer
2. Spelaren får val att ta fler kort "hit" eller stanna "stand
3. Spelaren kan fortsätta ta kort tills spelaren når 21 eller över
4. Om spelaren går över 21 poäng så förlorar spelaren direkt
5. När spelaren stannar, spelar datorn sin tur, Datorn måste ta 
kort så länge summan av korten är mindre än 17 och stanna när
datorns kortsumma är 17 poäng eller mer.
6. Om datorn går över 21 poäng vinner spelaren oavsett vilka
kort spelaren har
7. Om varken spelaren eller datorn går över 21 poäng så vinner
den som har högst kortsumma

'''

class Player:
    def __init__(self, user):

        self.user = user
        self.point = 0
        self.hand = []

    def display_hand(self):
        print(f"{self.user}'s hand: {self.hand} (Points: {self.point})")

    def reset(self):
        self.point = 0
        self.hand = []

class Cards(Player):
    def __init__(self):
        
        self.cardList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    #Random card that chooses from the list, aka 2-A
    def randomCards(self):
        card = random.choice(self.cardList)
        #print(card)
        return card

    #shows what card has been dealt to the player
    def cardPlayer(self, player):
       card = self.randomCards()
       player.hand.append(card)
       print(f"Dealt card: {card}")

    #1 and 11 are A. 12, 13, 14 are J Q and K
    def valueCard(self, card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
    
    #shows the points for the cards that has been dealt for the player
    def pointPlayer(self, player):
        player.point = 0
        ace_count = 0
        pHand = player.hand

        for i in pHand:
            player.point += self.valueCard(i)
            if i == 'A':
                ace_count += 1
        #print(player.point)

        while player.point > 21 and ace_count > 0:
            player.point -= 10 #Convert Ace from 11 to 1
            ace_count -= 1    

        return player.point

game = True

player1 = Player("Player 1")
player2 = Player("Dealer")
deck = Cards()


#Blackjack game starts here
while game:

    deck.cardPlayer(player1)
    deck.cardPlayer(player2)
    deck.cardPlayer(player1)

    deck.pointPlayer(player1)
    deck.pointPlayer(player2)

    player1.display_hand()
    player2.display_hand()

    if deck.pointPlayer(player1) == 21 and deck.pointPlayer(player2) != 11:
        print("You have BlackJack!")
        print("You won!")
        game = False

    while deck.pointPlayer(player1) < 21:
        action = input("Type 'hit' to take a card or 'stand' to stand: ")
        if action == "hit":
            deck.cardPlayer(player1)
            deck.pointPlayer(player1)
            player1.display_hand()
            if deck.pointPlayer(player1) > 21:
                print("You lose, too many cards")
                game = False
                break
        else:
            break

    while deck.pointPlayer(player2) < 17 and game == True:
        deck.cardPlayer(player2)
        deck.pointPlayer(player2)  
        player2.display_hand()

    if deck.pointPlayer(player2) > 21:
        print("You won, dealer busted too many cards")
        
    elif deck.pointPlayer(player1) > deck.pointPlayer(player2):
        print("You won against dealer")
        
    elif deck.pointPlayer(player1) == deck.pointPlayer(player2):
        print("You have push")
        
    else:
        print("You lost against dealer")
       

    rep = input("Do you want to play Blackjack again? (y/n): ")

    if rep == 'y':
        player1.reset()
        player2.reset()
        game = True
    else:
        game = False

    
    
    
