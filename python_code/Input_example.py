#WRITE A PROGRAM TO CONVERT POUNDS TO KG
#write a function to get a (positive) number from the user
def get_pos_float_input():
  user_weight = 0
  while(True):
    try:
      user_weight = float(input('enter your weight in pounds:'))
      #check if user weight is greater htna zero if not reprompt user
      if user_weight <= 0:
        print('ERROR: please enter weight greater than zero')
        continue
      else:
        break  
    except:
      print('ERROR: please enter a number greater than zero')
      
  return user_weight



#INPUT
#get weight from the user
user_weight = get_pos_float_input()
#ask a user to enter their weight in pounds and validate input
#if bad input repromt user

#use a conversion to convert pounds to kg: 2.205 lbs = 1kg
lbsPerKg = 2.205
#PROCESSING
user_weight_kg = user_weight / lbsPerKg
#OUTPUT
#print output to user
print(f'You weigh {user_weight_kg:.2f} kgs.')
#you weigh ___ kilos
