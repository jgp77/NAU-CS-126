import random
from operator import itemgetter
__author__='Natalie Jarusewski and Joshua Pollock'


def get_highscore(highscores):
    if len(highscores) == 0:
        print('There are no current high scores!')
        main(highscores)
    count=0
    while count <= (len(highscores) - 1):
        print(str(highscores[count][0]) + ': ' + str(highscores[count][1]))
        count += 1
    print('\n')
    main(highscores)

def save_highscore(score, name, highscores,questions):
    highscores.append((name, score))
    highscores=sorted(highscores, key=itemgetter(1), reverse=True)[:5]
    play_again=input('Do you want to play again? ').lower()
    if play_again == 'yes':
        playgame(questions)
    if play_again == 'no':
        main(highscores)


def playgame(questions):
    amount_correct=0
    # Creates the amount_correct variable to keep track of amount
    for num in range(0, 10):
        print(questions[num]['question'])
        print(' '.join(questions[num]['answers']))
        # Prints the questions and possible answers
        userschoice=input('Enter answer: ')
        if userschoice == (questions[num]['correct']):
            print('That is correct!')
            amount_correct += 1
            print('\n')
        # Asks the user to input an answer and checks if it is correct
        elif int(userschoice) not in range(0, len(questions[num]['answers'])):
            while userschoice not in range(0, len(questions[num]['answers'])):
                print('Please enter a correct choice: ')
                userschoice=input('Enter answer: ')
                if int(userschoice) not in range(
                        0, len(questions[num]['answers'])):
                    continue
                elif int(userschoice) in range(0,
                                               len(questions[num]['answers'])):
                    if userschoice == (questions[num]['correct']):
                        print('That was correct')
                        amount_correct += 1
                        print('\n')
                        break
                    elif userschoice != (questions[num]['correct']):
                        print('That is not correct! The correct answer is ' +
                              str((questions[num]['correct'])))
                        print('\n')
                        break
        # Checks to see if the user entered a valid response
        elif userschoice != (questions[num]['correct']):
            print('That is not correct! The correct answer is ' +
                  str((questions[num]['correct'])))
            print('\n')
            # Tells the user their response was incorrect
        print('Your current score is %d out of %d' % (amount_correct, num + 1))
        # Prints the current score
    print('\n')
    name=input('Input your name: ')
    save_highscore(amount_correct, name, highscores,questions)
    # Asks the user if they wish to play again and then sends them to desired
    # area


def game_credits():
    print('\n')
    print('This gameshow was created by Natalie Jarusewski and Joshua Pollock')
    print('Thank you for playing!')
    print('\n')
    main(highscores)


def main(highscores):
    questions=[
        {
            'question':
            "'Vulpes vulpes' is the scientific name for which animal?",
            'answers': [
                '0. Dog',
                '1. Cat',
                '2. Fox',
                '3. Lion'], 'correct':'2'}, {
            'question': 'What color are flamingos when they are born?',
            'answers': [
                '0. Pink', '1. Purple', '2. White'], 'correct': '2'}, {
            'question': 'What is the most endangered species in the world?',
            'answers': [
                '0. Amur Leopard',
                '1. Dodo Bird',
                '2. Ivory-Billed Woodpecker',
                '3. Tiger'],
            'correct': '2'}, {
            'question': 'What is the tallest tree species?',
            'answers': [
                '0. Coast Douglas Fir',
                '1. Coast Redwood',
                '2. Giant Sequoia'], 'correct': '1'}, {
            'question': 'What is the highest mountain range?',
            'answers': [
                '0. Himalayas',
                '1. Andes',
                '2. Hindu Kush',
                '3. Alps'], 'correct': '0'}, {
            'question': 'How many hours a day do koalas sleep?',
            'answers': [
                '0. 8', '1. 14', '2. 22', '3. 18'], 'correct': '3'}, {
            'question': 'How many electric volts can electric eels emit?',
            'answers': [
                '0. 400', '1. 600', '2. 800', '3. 1000'], 'correct': '1'}, {
            'question': 'How fast is the earth traveling around the sun?',
            'answers': [
                '0. 29,000 mph', '1. 67,000 mph', '2. 54,000', '3. 1,000,000'],
            'correct': '1'}, {
            'question': 'How old is the earth?', 'answers': [
                '0. 4.54 billion years old',
                '1. 3.24 billion years old',
                '2. 5.63 billion years old'],
            'correct': '0'}, {
            'question': 'What animal holds hands while they sleep?',
            'answers': [
                '0. Monkeys', '1. Otters', '2. Squirrels'], 'correct': '1'}]
    # Creates a dictionary to store the questions, answers, and correct choice
    random.shuffle(questions)
    # Shuffles the questions so it is random
    print('\nWelcome to our nature and animal game show!')
    print('Win a high five!\n')
    # Welcomes the user to our game

    menu=input('1. Play the game \n2. Game Credits\n3. Highscore\n4. Quit\n')
    if menu == '1':
        playgame(questions)
    if menu == '2':
        game_credits()
    if menu == '3':
        get_highscore(highscores)
    if menu == '4':
        exit
highscores=[]
main(highscores)
# Creates
