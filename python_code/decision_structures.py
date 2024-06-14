def get_int(prompt):
  input_value = 0
  while(True):
    try:
      input_value = int(input(prompt))
      if input_value > 12 or input_value <= 0:
        print('Please enter a value between 1 and 12')
        continue
    except:
      print('ERROR: please enter an integer')
      continue
    return input_value
def main():

  a=5
  b=7
  
  if a > b :
    print(f'{a} is greater than {b}.')
  elif a == b:
    print(f'{b} is equal to {a}')
  else:
    print(f'{b} is greater than {a}')

  #print the appropriate letter grade based on test score
  #A100-90 b89-80 c-79-70 d69-60 F60-0

  print('\nGrade Decision: 1 \n')
  test_score = 79.3

  if test_score <= 100 and test_score >= 90:
    print(f'{test_score} --> A')
  elif test_score < 90 and test_score >= 80:
    print(f'{test_score} --> B')
  elif test_score < 80 and test_score >= 70:
    print(f'{test_score} --> C')
  elif test_score < 70 and test_score >= 60:
    print(f'{test_score} --> D')
  else:
    print(f'{test_score} --> F')

  #grade desiciont restructure
  print('\nGrade Decision: 2 \n')
  if test_score <=100 and test_score >= 90:
    print(f'{test_score} --> A')
  elif test_score >= 80:
    print(f'{test_score} --> B')
  elif test_score >= 70:
    print(f'{test_score} --> C')
  elif test_score >= 60:
    print(f'{test_score} --> D')
  else:
    print(f'{test_score} --> F')

  #create a decision structure to determuine the season based on month
  #winter 12, 1, 2 Spring 3, 4, 5 Summer 6, 7, 8, fall 9, 10, 11
  #ask user to enter the number of the month then output the season based on the month
  user_month = get_int('What is the number of month you are in? ')

  if user_month in (1, 2, 12):
    print('Its is Winter!')
  elif user_month in (3, 4, 5):
    print('Its Spring!')
  elif user_month in (6, 7, 8):
    print('Its Summer!')
  else:
    print('Its Fall!')

main()