def main():
    #capitalize string
    my_name = 'rylan'
    print(my_name.capitalize())

    #make string upper case
    print(my_name.upper())

    #make a string lowercase
    last_name = 'DAVIS'
    print(f'{my_name.capitalize()} {last_name.lower()}')

    #determine if string starts with a set of characters
    print(my_name.startswith('R'))
    if(my_name.startswith('r') or my_name.startswith('R')):
        print(f'You spelled {my_name} correctly!')
    else:
        print(f'You spelled {my_name} wrong')

    #determine if a string ends with a specified set of characters
    print(my_name.endswith('lan'))
    
    #find a set of characters in a string
    print(my_name.find('a', 4))

    #loop through a string
    for letter in my_name:
        print(letter)

    print(f'{my_name} has {len(my_name)} letters')

    for letter_index in range(len(my_name)):
        print(f'Letter {letter_index}: {my_name[letter_index]}')

    print('\n\n')
    sentence = 'I have a dog. My dog is cute. Do you want a dog?'

    #write code that counts the number of occurences of the word dog in the sentence
    #expoected output = 3
    #use while loop to read string
    #read untill you find dog
    #add one to number of dogs
    #continue reading from that index by updating start index
    start_index = 0
    dog_number = 0
    while True:
        dog_index = sentence.find('dog', start_index)
        if dog_index == -1:
            break
        else:
            dog_number =+ 1
            start_index = dog_index + 1
            continue
    
       
    print(dog_number)

    #How to use the split method
    car_info = "Ferrari,f-50,2021,500000,4.8"

    car_data = car_info.split(',')
    print(car_data)

main()