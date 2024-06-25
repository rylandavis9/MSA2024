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

def get_percent(prompt):
  percent = 0
  while(True):
    try:
      percent = float(input(prompt))
      if percent <= 0:
        print('Error: you must enter a value greater than zero')
        continue
      else:
          break
    except:
      print('Error: Please enter a numerical value with no %')
      
  return percent

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

#ask user if they would like to save money
savings_amount = get_percent('What percent would you like to save? (no %)')

#turn % to decimal value
percent_savings = savings_amount / 100

#get saving amounts per month and year
yearly_savings = percent_savings * yearly_net_income
monthly_savings = yearly_savings / 12

#print savings advice
print(f'If you save {savings_amount}% you will want to save ${monthly_savings:.2f} per month, and ${yearly_savings:.2f} per year')

#get APR to calculate money earned from savings and turn to a percent
intrest_amount = get_percent('What is your APR (no %)')
percent_intrest = intrest_amount / 100
intrest = percent_intrest * yearly_savings
yearly_savings_with_intrest = intrest + yearly_savings

#print investment profit (kinda but not really how it actually works)
print(f'With an APR of {intrest_amount}% you will make ${intrest:.2f} over a year and your total saved will go to ${yearly_savings_with_intrest:.2f} (compounded yearly)')