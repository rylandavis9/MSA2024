def return_season():
  input_value = 0
  while(True):
    try:
      input_value = int(input('What is the number of month you are in? '))
      if input_value > 12 or input_value <= 0:
        print('Please enter a value between 1 and 12')
        continue
    except:
      print('ERROR: please enter an integer')
      continue

    if input_value in (1, 2, 12):
      season = 'Winter'
    elif input_value in (3, 4, 5):
      season = 'Spring'
    elif input_value in (6, 7, 8):
      season = 'Summer'
    else:
      season = 'Fall'

    return season

def main():
  while True:
    season = return_season()
    print(f'\nIt is {season}\n')
    
    run_again = input('would you like to run again? y or Y: ')
    if run_again == 'y' or run_again == 'Y':
      continue
    else:
      break
main()