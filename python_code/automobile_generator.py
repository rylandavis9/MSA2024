import automobile

def main():
    #create automobile object
    auto1 = automobile.Automobile('ford', 'focus', '1234', 2.2, 'alice', 2013 )
    auto2 = automobile.Automobile('honda', 'accord', '23456', 3.0, 'bob', 2017 )

    print(f'{auto1.make}')
main()