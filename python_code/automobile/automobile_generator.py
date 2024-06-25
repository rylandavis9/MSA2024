import automobile.automobile as automobile

def main():
    #create automobile object
    auto1 = automobile.Automobile('ford', 'focus', '1234', 2.2, 'linc', 2013 )
    auto2 = automobile.Automobile('honda', 'accord', '23456', 3.0, 'bob', 2017 )

    #print auto one and 2 data
    auto1.print_info()
    auto2.print_info()

    #change auto 2 engine size
    auto2.set_engine_size('2.4')

    #change auto one owner
    auto1.set_owner('Allie')

    auto1.print_info()
    auto2.print_info()

    #print car age info
    print(f'Auto1 is {auto1.get_age()} years old')
    print(f'Auto2 is {auto2.get_age()} years old')

    #create a list of automobiles
    automobile_list = []
    automobile_list.append(auto1)
    automobile_list.append(auto2)

    print('\nGetting automobiles from a list\n-------------------------------------')
    for auto in automobile_list:
        auto.print_info()
main()