def get_int(prompt):
  input_value = 0
  while(True):
    try:
      input_value = int(input(prompt))
    except:
      print('ERROR: please enter an integer')
      
    return input_value

def main():
  #print integers between 0 and 10
  for number in range(11):
    print(number)

  #print integers between 5 and 10
  print('\n\n')
  for number in range(5, 11):
    print(number)

  #print even numbers between 0 and 10
  print('\n\n')
  for number in range(0, 11, 2):
    print(number)
  print('\n\n')
  #prompt the user for start and stop values and print the numbers between start and stop
  #get start & stop value from user and convert to an integer

  start_value = get_int('Enter start value:')
  stop_value = get_int('Enter stop value:')

  for number in range(start_value, stop_value + 1):
    print(number)
    
main()