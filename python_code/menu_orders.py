#declare menu dictionary
#prompt for an item in a loop that lasts until end is called, 
#if end with lower string method to capitalize correctly
#check if user input is in the dictionary
#if is add value to total
#if not re prompt
def main():
  menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }
  price = 0
  while True:
    user_input = ''
    try:
      user_input = input('Item:\n')
      if user_input.title() == 'End':
        break
      elif user_input.title() in menu:
        price += menu[user_input.title()]
        print(f'Your total is ${price}')
      else:
        continue
    except:
      continue

main()