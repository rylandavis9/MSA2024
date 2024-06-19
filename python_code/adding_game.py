import random

#get level of game
def get_game_level():
    input_value = 0
    while(True):
        try:
            input_value = int(input('Enter level 1, 2, 3: '))
            if input_value > 3 or input_value < 1:
                print('Please enter level 1, 2, 3')
                continue
        except:
            print('ERROR: please enter an integer')
            continue
        return input_value
#get the number of problems
def get_num_of_problems():
    input_value = 0
    while(True):
        try:
            input_value = int(input('Enter number of games 3-10: '))
            if input_value > 10 or input_value < 3:
                print('Please enter amount between 3 and 10')
                continue
        except:
            print('ERROR: please enter an integer')
            continue
        return input_value
#create a function that i can easily edit for levels 2 and 3
#first get the amount of problems
#then for every problem print and find answer
#ask user for input for answer
def level_1():
    strikes = 0
    answer = 0
    total_questions = 0
    correct_answers = 0
    while True:
        problem_number = get_num_of_problems()
        value_one = random.randint(0, 9)
        value_two = random.randint(0, 9)
        try:
            if total_questions != problem_number:
                answer = value_one + value_two
                user_answer = int(input(f'What is the answer to {value_one} + {value_two}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    total_questions += 1
                    correct_answers += 1
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes == 3:
                        print(f'The answer was {answer}')
                        strikes = 0
                        total_questions += 1
                        
        except:
            continue
        return correct_answers 
#change the numbers for level 2 but keep everything else the same
def level_2():
    strikes = 0
    answer = 0
    while True:
        problem_number = get_num_of_problems()
        value_one = random.randint(10, 99)
        value_two = random.randint(10, 99)
        try:
            for i in range(problem_number):
                answer = value_one + value_two
                user_answer = int(input(f'What is the answer to {value_one} + {value_two}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes == 3:
                        print(f'The answer was {answer}')
                        strikes = 0
        except:
            continue
        return answer
#change the numbers for level 2 but keep everything else the same
def level_3():
    strikes = 0
    answer = 0
    while True:
        problem_number = get_num_of_problems()
        value_one = random.randint(100, 999)
        value_two = random.randint(100, 999)
        try:
            for i in range(problem_number):
                answer = value_one + value_two
                user_answer = int(input(f'What is the answer to {value_one} + {value_two}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes == 3:
                        print(f'The answer was {answer}')
                        strikes = 0
        except:
            continue
        return answer

def main():
    while True:
        level = get_game_level()
        if level == 1:
            level1 = level_1()
        elif  level == 2:
            level2 = level_2()
        elif level == 3:
            level3 = level_3()

main()