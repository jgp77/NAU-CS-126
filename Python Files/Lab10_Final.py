import random
__author__='Natalie Jarusewski and Joshua Pollock'


class Card:

    suits=['Spades', 'Hearts', 'Clubs', 'Diamonds']
    face_cards=['Ace', 'King', 'Queen', 'Jack']
    # Creates two lists which contain the suits and face card names

    def __init__(self, card_num):
        '''
        Sets self.card_num to the current card
        number and sets the card to face up
        '''
        self.card_num=card_num
        self.down=False

    def get_suit(self):
        '''
    Gets the card's suit based off a range of numberArray. Calls the suit list
    based and returns the correct suit based off the range
        '''
        if self.card_num in range(0, 13):
            return(Card.suits[0])
        if self.card_num in range(13, 27):
            return (Card.suits[1])
        if self.card_num in range(27, 39):
            return (Card.suits[2])
        if self.card_num in range(39, 52):
            return (Card.suits[3])

    def get_rank(self):
        # If Ace card
        if self.card_num in [0, 13, 26, 39]:
            return Card.face_cards[0]
        # If 2 card
        if self.card_num in [1, 14, 27, 40]:
            return '2'
        # If 3 card
        if self.card_num in [2, 15, 28, 41]:
            return '3'
        # If 4 card
        if self.card_num in [3, 16, 29, 42]:
            return '4'
        # If 5 card
        if self.card_num in [4, 17, 30, 43]:
            return '5'
        # If 6 card
        if self.card_num in [5, 18, 31, 44]:
            return '6'
        # If 7 card
        if self.card_num in [6, 19, 32, 45]:
            return '7'
        # If 8 card
        if self.card_num in [7, 20, 33, 46]:
            return '8'
        # If 9 card
        if self.card_num in [8, 21, 34, 47]:
            return '9'
        # If 10 card
        if self.card_num in [9, 22, 35, 48]:
            return '10'
        # If Jack card
        if self.card_num in [10, 23, 36, 49]:
            return Card.face_cards[3]
        # If Queen card
        if self.card_num in [11, 24, 37, 50]:
            return Card.face_cards[2]
        # If King card
        if self.card_num in [12, 25, 38, 51]:
            return Card.face_cards[1]

    def get_value(self):
        '''
Gets the card value based off of given values from the lab.
Face cards are worth 10,Ace is worth 11, and number
cards are worth their number
        '''
        # If Ace Card
        if self.card_num in [0, 13, 27, 39]:
            return 11
        # If 2 Card
        if self.card_num in [1, 14, 28, 40]:
            return 2
        # If 3 Card
        if self.card_num in [3, 15, 29, 41]:
            return 3
        # If 4 Card
        if self.card_num in [4, 16, 30, 42]:
            return 4
        # If 5 Card
        if self.card_num in [5, 17, 31, 43]:
            return 5
        # If 6 Card
        if self.card_num in [6, 18, 32, 44]:
            return 6
        # If 7 Card
        if self.card_num in [7, 19, 33, 45]:
            return 7
        # If 8 Card
        if self.card_num in [8, 20, 34, 46]:
            return 8
        # If 9 Card
        if self.card_num in [9, 21, 35, 47]:
            return 9
        # If 10 Card
        if self.card_num in [10, 22, 36, 48]:
            return 10
        # If Jack Card
        if self.card_num in [11, 23, 37, 49]:
            return 10
        # If Queen Card
        if self.card_num in [12, 24, 38, 50]:
            return 10
        # If King Card
        if self.card_num in [13, 25, 39, 51]:
            return 10

    def face_down(self):
        '''
Sets the card orientation to face down.
        '''
        self.down=True

    def face_up(self):
        '''
Sets the card orientation to face up.
        '''
        self.down=False

    def __str__(self):
        '''
Checks to see if the card is face down
or face up. Based off that it will eithier
print the card, or print <facedown>.
        '''
        if not self.down:
            suit=str(self.get_suit())
            rank=str(self.get_rank())
            return(rank + ' of ' + suit)

        elif self.down:
            return('<facedown>')


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


if __name__ == '__main__':
    deck=[]
    for i in range(52):
        my_card=Card(i)
        deck.append(my_card)
        print(my_card)
    print(random.choice(deck))
    card=Card(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)
    card.face_up()
    print(card)

    cs=ChipBank(149)
    cs.record('logging.txt')
    print(cs)
    cs.deposit(7)
    print(cs.value)
    print(cs)
    print(cs.withdraw(84))
    print(cs)
    cs.deposit(120)
    print(cs)
    print(cs.withdraw(300))
    cs.record(None)

    f=open('logging.txt', 'r+')
    lines=f.readlines()
    print('Reading file... ')
    for line in lines:
        print(line)

    f.close()
