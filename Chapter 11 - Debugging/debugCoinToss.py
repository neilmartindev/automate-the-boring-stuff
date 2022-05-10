import random
import logging 
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - '
                '%(levelname)s - %(message)s') 

logging.debug('Start of solution')
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess logging')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('Start of toss')
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 0:
    print('tails')
    toss = 'tails'
if toss == 1:
    print('heads')
    toss = 'heads'

    logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')  # not in original code

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')