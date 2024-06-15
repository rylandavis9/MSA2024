def get_int(prompt):
  insert_coin = 0
  while True:
    try:
      insert_coin = int(input(prompt))
      if insert_coin < 0:
        print('You cannot put negative coins in this machine.')
        continue
      elif insert_coin not in [1, 5, 10, 25]:
        continue
      elif insert_coin in [1, 5, 10, 25]:
       break
    except:
      print('ERROR: please enter an integer')
      
  return insert_coin
  
def vending_machine():
  due = 50
  while True:
    if due < 0:
      print(f'Change Owed: {due * -1}')
      break
    else:
      print(f'Vending Machine\n----------------\nAmount Due: {due}')
      insert_coin = get_int('Insert Coin:')
      due = due - insert_coin
  
def main():

  while True:
      machine = vending_machine()
      
      run_again = input('would you like to run again? y or Y: ')
      if run_again == 'y' or run_again == 'Y':
        continue
      else:
        break

main()