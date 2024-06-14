# function to add to numbers
#inpuy will be number_1 (int) and (int number_2)
#outputg will be total of thise numbers (int)
def add_numbers(number_1, number_2):
  total = number_1 + number_2
  c = 7
  return total

def main():
  a = 5
  b = 4
  c = 3
  #call add_numbers and assign the returned value to answer
  answer = add_numbers(a, b)
  print(f'{a} + {b} = {answer}')
  print(f"variable c = {c}")
  
main()