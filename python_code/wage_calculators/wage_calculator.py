#declare constants
workdays_per_yr = 350
tax = 0.88 #100% - 12% = 88% of the original
tax_string = '12%'

#create (reuse) function to keep inputs as numbers
def get_nonnegative_float(prompt, must_be_less_than_24):
  input_value = 0
  while(True):
    try:
      input_value = float(input(prompt))
      #check if user wage is greater than zero if not reprompt user
      if input_value <= 0:
        print('ERROR: please enter value greater than zero')
        continue
      if(input_value > 24 and must_be_less_than_24):
        print('ERROr: you cannot work more than 24 hours in a day.')
        continue
      break  
    except:
      print('ERROR: please enter a number')
      
  return input_value

#ask User for hours worked (daily) and wage
user_wage = get_nonnegative_float('Enter hourly wage: ', False)
user_hours = get_nonnegative_float('Enter hours per day: ', True)

#calculate by doing hours*wage*350*0.12
#calculate yearly hours as well

yearly_hours = user_hours * workdays_per_yr
yearly_gross_income = user_wage * user_hours * workdays_per_yr
yearly_net_income = yearly_gross_income * tax

#Print pay advice

print(f'Pay Advice: \n--------------------------------- \n In one year you will work {user_hours} hours per day, {yearly_hours} hours per year,\n getting payed ${user_wage:.2f} per hour.\n Your gross income per year is ${yearly_gross_income:.2f}.\n You get taxed {tax_string}.\n Your yearly income after taxes is ${yearly_net_income:.2f}')
