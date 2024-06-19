def main():
  while True:
    user_input = 0
    answer = 0
    try:
      user_input = input('Enter an expression (x +-*/ Y) or end to stop: ')
      if user_input.title() == 'End':
        break
      user_input = user_input.split(' ')
      if len(user_input) == 3:
        if user_input[1] == '/' and user_input[2] == '0':
          print('Cannot divide by 0')
          continue
        elif user_input[1] == '+':
          answer = int(user_input[0]) + int(user_input[2])
        elif user_input[1] == '-':
          answer = int(user_input[0]) - int(user_input[2])
        elif user_input[1] == '*':
          answer = int(user_input[0]) * int(user_input[2])
        elif user_input[1] == '/':
          answer = int(user_input[0]) / int(user_input[2])
        print(f'{answer:.1f}')
      else:
        continue
    except:
      continue

main()