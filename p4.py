"""
4. Number Guessing Game

Concepts: random, loops, condition

Features:

random number generate - done
limited attempts - done
hint system -done
score system - done
save scores in csv - done

Extra:

difficulty mode
"""
#import random module for generate a random number, it also can be done by numpy
import random as rd

#scoring function

def scoring(q):
    point = 100 - abs(random_number - q)
    score.append(point)

#hints
def hints(p):
    if 1 <= random_number - p <= 5:
        print('You\'re extremely close (add 1 to 5)')
    elif -5 <= random_number - p <= -1:
        print('You\'re extremely close (subtract 1 to 5)')
    elif 15 <= random_number - p <= 30:
        print('You\'re far from 15 to 30, you should add more')
    elif -30 <= random_number - p <= -15:
        print('You\'re far from 15 to 30, you should subtract more')
    elif 40 >= random_number - p >= 31:
        print('You\'re very far from the number (add between 30-40)')
    elif -40 <= random_number - p <= -31:
        print('You\'re very far from the number (subtract between 30-40)')
    elif random_number % 2 == 1 and p % 2 == 0:
        print('It\'s an Odd number')
    elif random_number % 2 == 0 and p % 2 == 1:
        print('It\'s an EVEN number')
    elif p < random_number:
        print('Correct number is higher than yours')
    elif p > random_number:
        print('Correct number is lower than yours')


if __name__ == "__main__": #main program start from here, and can't be imported from other file

    mode = input('1.Easy\n2.Normal\n3.Difficult\n')
    if mode == '1':
        random_number = rd.randint(1, 10)
    elif mode == '2':
        random_number = rd.randint(1, 50)
    else:
        random_number = rd.randint(1, 100)

    user_name = input('Enter your name\n')
    if user_name.isalpha():
        score = []

        count = 0
        while count <=2:
            x = int(input('Guess a number [Easy:1-10, Normal:1-50, Difficult:1-100]\n'))
            if random_number == x:
                print('*** WINNER ***')
                scoring(x)
                break
            else:
                if count <= 1: #skip giving hints for last time
                    hints(x)
                scoring(x)
                count += 1
        if count == 3:
            print("Sorry!, Try next time.")


        max_score = max(score)

        s_board = {}

        with open('board.csv', 'r') as f:
            next(f)
            for i in f:
                x , y = i.split(',')
                y = (str(y)).replace('\n', '')
                y = int(y)
                s_board[x] = y

        s_board[user_name] = max_score



        print(f'Total score is, {max_score},\nRandom number was, {random_number}')
        save_print = input('1.Save\n2.Print only\n')
        if save_print == '1':
            with open('board.csv', 'w') as r:
                r.write(f'Name,Score\n')
                for m,n in s_board.items():
                    r.write(f'{m},{n}\n')
        else:
            print(s_board)

    else:
        print('Invalid Name')
   