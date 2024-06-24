import random

def main():
    
    #print a random number between 1 and 10
    print('random number: 1-10')
    random_value = random.randint(1, 10)
    print(f'random value: {random_value}')

    #generate 10 random numbers between 1 and 10
    for i in range(10):
        print(f'Random number {i + 1}: {random.randint(1,10)}')

    #choose random value from list of values
    print('\n Choose random value from list\n-----------------------------------------------')
    rand_list = [1, 4, 5, 6, 3, 7, 12, 78, 99, 69, 918]
    random_index = random.randint(0, len(rand_list) -1)
    print(random_index)
    print(f'random list value: {rand_list[random_index]}')

    #ask user fro start and stop values to generate a random number between
    #ask user how many random numbers to generate and generate thaqt many random numbers
    print('\n User generated random numbers\n------------------------------')
    start_value = int(input('enter start value: '))
    stop_value = int(input('enter stop value: '))
    total_numbers = int(input('enter total numbers to be generated: '))
    for i in range(total_numbers):
        print(f'random number {i + 1}: {random.randint(start_value, stop_value)}')
    
main()