import random
__blackjack_and_blackjackhand_authors__='Alec and Joshua Pollock'
__card_and_chipbank_authors__='Natalie Jarusewski and Joshua Pollock'


class Card:

    suits=['Spades', 'Hearts', 'Clubs', 'Diamonds']
    face_cards=['Ace', 'King', 'Queen', 'Jack']

    def __init__(self, card_num):
        self.card_num=card_num
        self.down=False

    def get_suit(self):

        if self.card_num in range(0, 13):
            return Card.suits[0]
        if self.card_num in range(13, 27):
            return Card.suits[1]
        if self.card_num in range(27, 39):
            return Card.suits[2]
        if self.card_num in range(39, 52):
            return Card.suits[3]

    def get_rank(self):
        if self.card_num in [0, 13, 26, 39]:
            return Card.face_cards[0]
        if self.card_num in [1, 14, 27, 40]:
            return '2'
        if self.card_num in [2, 15, 28, 41]:
            return '3'
        if self.card_num in [3, 16, 29, 42]:
            return '4'
        if self.card_num in [4, 17, 30, 43]:
            return '5'
        if self.card_num in [5, 18, 31, 44]:
            return '6'
        if self.card_num in [6, 19, 32, 45]:
            return '7'
        if self.card_num in [7, 20, 33, 46]:
            return '8'
        if self.card_num in [8, 21, 34, 47]:
            return '9'
        if self.card_num in [9, 22, 35, 48]:
            return '10'
        if self.card_num in [10, 23, 36, 49]:
            return Card.face_cards[3]
        if self.card_num in [11, 24, 37, 50]:
            return Card.face_cards[2]
        if self.card_num in [12, 25, 38, 51]:
            return Card.face_cards[1]

    def get_value(self):
        if self.card_num in [0, 13, 26, 39]:
            return 11
        if self.card_num in [1, 14, 27, 40]:
            return 2
        if self.card_num in [2, 15, 28, 41]:
            return 3
        if self.card_num in [3, 16, 29, 42]:
            return 4
        if self.card_num in [4, 17, 30, 43]:
            return 5
        if self.card_num in [5, 18, 31, 44]:
            return 6
        if self.card_num in [6, 19, 32, 45]:
            return 7
        if self.card_num in [7, 20, 33, 46]:
            return 8
        if self.card_num in [8, 21, 34, 47]:
            return 9
        if self.card_num in [9, 22, 35, 48]:
            return 10
        if self.card_num in [10, 23, 36, 49]:
            return 10
        if self.card_num in [11, 24, 37, 50]:
            return 10
        if self.card_num in [12, 25, 38, 51]:
            return 10

    def ace_get_value(self):
        if self.card_num in [0, 13, 26, 39]:
            return 1
        if self.card_num in [1, 14, 27, 40]:
            return 2
        if self.card_num in [2, 15, 28, 41]:
            return 3
        if self.card_num in [3, 16, 29, 42]:
            return 4
        if self.card_num in [4, 17, 30, 43]:
            return 5
        if self.card_num in [5, 18, 31, 44]:
            return 6
        if self.card_num in [6, 19, 32, 45]:
            return 7
        if self.card_num in [7, 20, 33, 46]:
            return 8
        if self.card_num in [8, 21, 34, 47]:
            return 9
        if self.card_num in [9, 22, 35, 48]:
            return 10
        if self.card_num in [10, 23, 36, 49]:
            return 10
        if self.card_num in [11, 24, 37, 50]:
            return 10
        if self.card_num in [12, 25, 38, 51]:
            return 10

    def face_down(self):
        self.down=True

    def face_up(self):
        self.down=False

    def __str__(self):
        if not self.down:
            suit=str(self.get_suit())
            rank=str(self.get_rank())
            return rank + ' of ' + suit

        elif self.down:
            return'<facedown>'


class ChipBank():
    logging=0

    def __init__(self, value):
        self.value=value

    def withdraw(self, amount):
        if amount <= self.value:
            self.value -= amount
            if ChipBank.logging == 1:
                self.bank.write(str(self.value) + ' -' + str(amount) + '\n')
            return amount

        elif amount > self.value:
            withdrawn=self.value
            self.value=0
            if ChipBank.logging == 1:
                self.bank.write(str(self.value) + ' -' + str(withdrawn) + '\n')
            return withdrawn

    def deposit(self, amount):
        self.value += amount
        if ChipBank.logging == 1:
            self.bank.write(str(self.value) + ' +' + str(amount) + '\n')

    def __str__(self):
        current_amount=self.value
        green=0
        blacks=0
        red=0
        if current_amount >= 100:
            blacks=current_amount // 100
            current_amount %= 100
        if current_amount >= 25:
            green=current_amount // 25
            current_amount %= 25
        if current_amount >= 5:
            red=current_amount // 5
            current_amount %= 5
        return ('The total value is ' +
                str(self.value) + '\n' +
                'Black Chips : ' +
                str(blacks) + '\n' +
                'Green Chips: ' +
                str(green) + '\n' +
                'Red Chips: ' +
                str(red) + '\n' +
                'Blue Chips: ' +
                str(current_amount))

    def record(self, handle):
        if handle is None:
            self.bank.close()
            ChipBank.logging=0
        else:
            self.bank=open(handle, 'w')
            ChipBank.logging=1


class BlackJackHand():

    def __init__(self):
        # Initializes a blank list for the hands
        self.hand=[]

    def add_card(self, new_card):
        # Adds a card to the hand
        self.hand.append(new_card)

    def __str__(self):
        # Prints out the deck and returns nothing
        for i in self.hand:
            print(i)
        return ''


class BlackJack():
    bank=ChipBank(0)
    # Sets up a variable to keep track of chips

    def __init__(self, starting_dollars, simulated):
        ''' Initializes all the needed items for the BlackJack class.
        Creates a deck of cards, using the Card class, and
        then shuffles the created deck
        '''
        self.wager=0
        self.simulated=simulated
        BlackJack.bank.deposit(starting_dollars)
        self.player_hand=BlackJackHand()
        self.dealer_hand=BlackJackHand()
        self.player_total=0
        self.dealer_total=0
        self.deck=[]
        self.hand_counter=0
        if self.simulated:
            BlackJack.bank.record('simulation.txt')
        for i in range(52):
            self.deck.append(Card(i))
        random.shuffle(self.deck)

    def draw(self):
        '''Checks to see if the deck has enough
        cards for a round, and if not, it will
        recreate and shuffle the deck'''
        if len(self.deck) < 15:
            self.deck=[]
            for i in range(52):
                self.deck.append(Card(i))
            random.shuffle(self.deck)

    def start_hand(self, wager):
        self.player_total=0
        self.dealer_total=0
        # Resets each total to 0
        self.wager=wager
        # Sets up the wager
        self.player_hand.add_card(self.deck.pop(0))
        self.dealer_hand.add_card(self.deck.pop(0))
        self.player_hand.add_card(self.deck.pop(0))
        self.dealer_hand.add_card(self.deck.pop(0))
        # Creats the starting hand for player and dealer
        self.player_total=self.player_hand.hand[
            0].get_value() + self.player_hand.hand[1].get_value()
        self.dealer_total=self.dealer_hand.hand[
            0].get_value() + self.dealer_hand.hand[1].get_value()
        # Sets up the dealer and player totals based off the generated hand
        self.dealer_hand.hand[0].face_down()
        # Sets the dealer's first card face down
        print("\nYour Hand: ")
        for i in self.player_hand.hand:
            print(i)
        print("\nDealer's Hand: ")
        for i in self.dealer_hand.hand:
            print(i)
        # Prints out the player and dealer hands
        if self.dealer_total == 21:
            # Checks for dealer blackjakc, but also makes sure the player did
            # not blackjack as well
            self.dealer_hand.hand[0].face_up()
            if self.dealer_total == self.player_total:
                print('\nDealer and Player Blackjack! Tie!')
                self.end_hand('push')
            print("\nDealer's Hand: ")
            for i in self.dealer_hand.hand:
                print(i)
            print("\nDealer Blackjack!!")
            self.end_hand('lose')
        elif self.player_total == 21:
            # Checks for player blackjack
            print("\nYour Hand: ")
            for i in self.player_hand.hand:
                print(i)
            print("\nPlayer Blackjack!!")
            self.end_hand('win')

    def game_active(self):
        # Checks to see if there is still money in the bank
        if BlackJack.bank.value >= 26000 and self.simulated:
            return False
        elif BlackJack.bank.value != 0:
            return True
        else:
            return False

    def hit(self):
        self.player_hand.add_card(self.deck.pop(0))
        self.player_total += self.player_hand.hand[-1].get_value()
        # Adds a card to the player's hand, and adds it to the total
        print('\nPlayer Hits!')
        if self.player_total > 22:
            self.player_total=0
            for i in self.player_hand.hand:
                self.player_total += i.ace_get_value()
        # Checks for player bust, and if the player has an ace
        print("\nYour Hand: ")
        for i in self.player_hand.hand:
            print(i)
        # Prints the new hand
        if self.player_total > 21:
            print('\nBust!')
            self.end_hand('lose')
        # Checks again for player bust

    def stand(self):
        self.dealer_hand.hand[0].face_up()
        # Flips over dealers 1st card
        print("\nDealer's Hand: ")
        # Prints dealer hand with the card flipped over
        for i in self.dealer_hand.hand:
            print(i)
        if self.dealer_total > self.player_total:
            # Checks to see if the dealer won
            print('\nDealer Wins!')
            self.end_hand('lose')
        else:
            while self.dealer_total < 17:
                # While the dealer total is less than 17
                self.dealer_hand.add_card(self.deck.pop(0))
                print('\nDealer Hits!')
                self.dealer_total += self.dealer_hand.hand[-1].get_value()
                # Adds new card to dealer total
                if self.dealer_total > 22:
                    # Checks to see if dealer's total is over 21. If it is,
                    # checks for an ace.
                    self.dealer_total=0
                    for i in self.dealer_hand.hand:
                        self.dealer_total += i.ace_get_value()
                print("\nDealer's Hand: ")
                for i in self.dealer_hand.hand:
                    print(i)
            '''Checks to see the outcome of the hand. Ends the hand based on
            the outcome'''
            if self.dealer_total == self.player_total:
                print('\nTie! Player Push!')
                self.end_hand('push')
            elif self.dealer_total > 21:
                print('\nDealer Bust!')
                self.end_hand('win')
            elif self.dealer_total > self.player_total:
                print('\nDealer Wins')
                self.end_hand('lose')
            elif self.dealer_total < self.player_total:
                print('\nDealer Stands! Player Wins!')
                self.end_hand('win')

    def end_hand(self, outcome):
        ''' Deposits or withdraws money based on the given outcome.
        The hand is then restarted if there is money left'''
        if outcome == 'win':
            BlackJack.bank.deposit((self.wager * 2))
        elif outcome == 'lose':
            BlackJack.bank.withdraw(self.wager)
        if BlackJack.bank.value >= 26000 and self.simulated:
            self.game_active()

        elif BlackJack.bank.value == 0:
            self.game_active()
        elif BlackJack.bank.value != 0:
            print('\nYour remaining chips: ' + str(BlackJack.bank))
            self.draw()
            if not self.simulated:
                while True:
                    # Creates a loop for checking purposes
                    try:
                        # Attempts to set a wager
                        wager=int(
                            input('How much would you like to wager?: '))
                        while wager > BlackJack.bank.value:
                            # Checks to see if the wager is
                            # greater than current
                            # amount of money
                            print('You do not have that much money!')
                            wager=int(
                                input(
                                    ('Please enter an amount that ' +
                                     'correspondes to your current chips: ')))
                        break
                    except:
                        print(
                            'Error! That amount is not' +
                            ' a correct input! Try Again!')
            elif self.simulated:
                self.hand_counter += 1
                wager=5
            while len(self.player_hand.hand) > 0:
                self.player_hand.hand.pop(0)
            while len(self.dealer_hand.hand) > 0:
                self.dealer_hand.hand.pop(0)
            self.start_hand(wager)

if __name__ == '__main__':
    while True:
        print('Welcome to Blackjack!')
        menu=input('PLAY, SIMULATION, or EXIT?: ').upper()
        if menu == 'PLAY':
            blackjack=BlackJack(250, False)
            while blackjack.bank.value > 0:
                print('Your remaining chips: ' + str(blackjack.bank))
                while True:
                    # Creates a loop for checking purposes
                    try:
                        # Attempts to set a wager
                        wager=int(
                            input('How much would you like to wager?: '))
                        while wager > blackjack.bank.value:
                            # Checks to see if the wager is
                            # greater than current amount
                            # of money
                            print('You do not have that much money!')
                            wager=int(
                                input(
                                    ('Please enter an amount that' +
                                     ' correspondes to your current chips: ')))
                        break
                    except:
                        # Informs the user if an incorrect input is entered
                        print('Error! That amount is not ' +
                              'a correct input! Try Again!')
                blackjack.start_hand(wager)
                while blackjack.game_active():
                    choice=input('\nSTAND or HIT?: ').upper()
                    if choice == 'STAND':
                        blackjack.stand()
                    elif choice == 'HIT':
                        blackjack.hit()
                print()
            print('Out of money! The casino wins!')
        elif menu == 'SIMULATION':
            simulation=BlackJack(1000, True)
            while simulation.bank.value > 0 and simulation.game_active():
                print('Remaining chips: ' + str(simulation.bank))
                simulation.start_hand(5)
                while simulation.game_active():
                    if simulation.player_total < 17:
                        simulation.hit()
                    if simulation.player_total >= 17:
                        simulation.stand()
                print()
            print('Simulation has won over $25,000. Ending Simulation!')
            print('Hands simulation has ran through: ' +
                  str(simulation.hand_counter))
            print('Simulation complete!\n')

        elif menu == 'EXIT':
            print('Thanks for playing!')
            break
        else:
            print('I did not understand you input! Try again!')
