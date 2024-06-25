#create program that accepts a highway number and outputs the direction
#user enters 95 output is interstate 95 runs south to north
#error check program so it does not crash
def get_int(prompt):
  input_value = 0
  while True:
    try:
      input_value = int(input(prompt))
      if input_value <= 0:
        print('Please enter a value greater than zero')
        continue
      elif input_value > 500:
        print('please enter a value less than 500')
        continue
      else:
        break
    except:
      print('ERROR: please enter an integer')
      
    return input_value
  
# ask for input value to be globally used by multiple functions.
input_value = get_int('What highway are you on?')

#check for remainder, If returned false it is not even
def check_even():
  remainder = 0
  is_even = False
  while True:
    try:
      remainder = input_value % 2
      if remainder == 1:
        is_even = False
      elif remainder == 0:
        is_even = True
    except:
      if input_value == 1:
        is_even = False
      print('something went wrong.')
#return the value of is_even for main
    return is_even
  
#put everything together
def main():
  is_even = check_even()
  if is_even == False:
    print(f'Interstate {input_value} runs East to West')
  elif is_even == True:
    print(f'Interstate {input_value} runs South to north')
  else:
    print()
main()
