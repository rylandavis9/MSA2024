def main():
  #list demo
  #create a list of string names
  names = ['rylan', 'allie', 'lincoln', 'kian']
  list_of_integers = [1, 2, 3, 4, 7, 10, 123, 457, 45, 1]
  random_type_list = ['noah', 15, 22.6, 'joe']

  print(names)
  print(list_of_integers)

  #add values to a list
  names.append('andrew')
  list_of_integers.append(5)
  list_of_integers.append(59)

  #reprint lists
  print(names)
  print(list_of_integers)

  #get number of items in a list
  number_of_items = len(list_of_integers)
  print(f'\n\nnumber of items in list of integers: {number_of_items}')

  #get values from our list
  #get the first value from the list of integers
  print(f'\nFirst item in integer list: {list_of_integers[0]}')

  #get the fourth value from the list of integers
  print(f'\nFourth item in integer list: {list_of_integers[3]}')
  
  #print all items in list of integers
  print('\ninteger list items')
  for item in list_of_integers:
    print(item)

  print('\n')
  # get # of items in integer list
  number_of_items = len(list_of_integers)

  for index in range(number_of_items):
    print(f'Item {index + 1}: {list_of_integers[index]}')

main()