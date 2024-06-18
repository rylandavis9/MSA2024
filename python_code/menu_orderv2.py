#function to loaf menu i9tems from menu.txt to create a dictionary
#input none
#output dictionary of menu items
def get_menu_items():
  #create file handle that gives file access
  data_file = open('menu.txt', 'r')
  #create empty dictionary to store menu items and prices
  menu_items = {}
  #loop through data in the file and read file one line at a time
  for line_of_data in data_file:
    #split the line of data at the , using .split
    keys_and_values = line_of_data.split(',')
    #get item and price from the resulting list and store in the dictionary
    item = keys_and_values[0]
    price = float(keys_and_values[1])
    menu_items[item] = price
  #close the file
  data_file.close()

  return menu_items

def main():
  #load the menu items dictionary
  menu_items = get_menu_items()
  price = 0
  while True:
    user_input = ''
    try:
      user_input = input('Item:\n')
      if user_input.title() == 'End':
        break
      elif user_input.title() in menu_items:
        price += menu_items[user_input.title()]
        print(f'Your total is ${price}')
      else:
        continue
    except:
      continue

main()