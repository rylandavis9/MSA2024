def main():
  while True:
    user_input = 0
    answer = 0
    try:
      user_input = input('Enter an expression(x _ Y): ')
      user_input = user_input.split(' ')
      if len(user_input) == 3:
        if user_input[1] == '+':
          answer = user_input[0] + user_input[2]
        elif user_input[1] == '-':
          answer = user_input[0] - user_input[2]
        elif user_input[1] == '*':
          answer = user_input[0] * user_input[2]
        elif user_input[1] == '/':
          answer = user_input[0] / user_input[2]
        print(answer)
      else:
        continue
    except:
      continue

main()