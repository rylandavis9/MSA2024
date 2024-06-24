#create variables to store name, age, & weight
# 'assignment statements'
first_name = 'Rylan'
last_name = 'Davis'
age = 15
half_age = age / 2
weight = 114.5

#say hello
print('Hello World')

#print name
print('My name is', first_name, sep='---')

#print full name
print('My full name is', first_name, last_name, sep='---')

#print a sentence with name, age, & weight
print(f'My name is {first_name} {last_name}.\nI am {age} years old and I weigh {weight}lbs')

#get and print data type for age, weigh, & half_age
print(type(age))
print(type(weight))
print(type(half_age))

#3 print statements with string interpolation to print descriptive sentences for the datatypes

print(f'Variable age is a {type(age)}')
print(f'Variable weight is a {type(weight)}')
print(f'Variable half_age is a {type(half_age)}')