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
    problem_number = get_num_of_problems()
    value_one = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    value_two = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    while True:
        try:
            if total_questions != problem_number:
                answer = value_one[total_questions] + value_two[total_questions]
                user_answer = int(input(f'What is the answer to {value_one[total_questions]} + {value_two[total_questions]}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    total_questions += 1
                    correct_answers += 1
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes >= 3:
                        print(f'The answer was {answer}')
                        strikes = 0
                        total_questions += 1
                continue
            else:
                level_ans = correct_answers / total_questions
                output = f'You did {total_questions} and got {correct_answers} correct. \n That is {(level_ans * 100):.2f}%'
        except:
            print('ERROR: please enter an integer')
            strikes +=1
            if strikes >= 3:
                print(f'The answer was {answer}')
                strikes = 0
                total_questions += 1
            continue
        return output 
#change the numbers for level 2 but keep everything else the same
def level_2():
    strikes = 0
    answer = 0
    total_questions = 0
    correct_answers = 0
    problem_number = get_num_of_problems()
    value_one = [random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99)]
    value_two = [random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99)]
    while True:
        try:
            if total_questions != problem_number:
                answer = value_one[total_questions] + value_two[total_questions]
                user_answer = int(input(f'What is the answer to {value_one[total_questions]} + {value_two[total_questions]}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    total_questions += 1
                    correct_answers += 1
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes >= 3:
                        print(f'The answer was {answer}')
                        strikes = 0
                        total_questions += 1
                continue
            else:
                level_ans = correct_answers / total_questions
                output = f'You did {total_questions} and got {correct_answers} correct. \n That is {(level_ans * 100):.2f}%'
        except:
            print('ERROR: please enter an integer')
            strikes +=1
            if strikes >= 3:
                print(f'The answer was {answer}')
                strikes = 0
                total_questions += 1
            continue
        return output 
#change the numbers for level 2 but keep everything else the same
def level_3():
    strikes = 0
    answer = 0
    total_questions = 0
    correct_answers = 0
    problem_number = get_num_of_problems()
    value_one = [random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)]
    value_two = [random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)]
    while True:
        try:
            if total_questions != problem_number:
                answer = value_one[total_questions] + value_two[total_questions]
                user_answer = int(input(f'What is the answer to {value_one[total_questions]} + {value_two[total_questions]}:'))
                if user_answer == answer:
                    print('CORRECT!!!')
                    total_questions += 1
                    correct_answers += 1
                    continue
                elif user_answer != answer:
                    strikes += 1
                    print('WRONG!!!')
                    if strikes >= 3:
                        print(f'The answer was {answer}')
                        strikes = 0
                        total_questions += 1
                continue
            else:
                level_ans = correct_answers / total_questions
                output = f'You did {total_questions} and got {correct_answers} correct. \n That is {(level_ans * 100):.2f}%'
        except:
            print('ERROR: please enter an integer')
            strikes +=1
            if strikes >= 3:
                print(f'The answer was {answer}')
                strikes = 0
                total_questions += 1
            continue
        return output 

def main():
    while True:
        level = get_game_level()
        if level == 1:
            level_ans = level_1()
        elif  level == 2:
            level_ans = level_2()
        elif level == 3:
            level_ans = level_3()
        print(level_ans)

main()