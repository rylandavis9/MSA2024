def main():
    scores = [1, 4, 6, 7, 78]
    student_names = ['Allie', 'Lincoln', 'Kian', 'Noah', 'Andrew']
    for index in range(len(scores)):
        print(f'{student_names[index]}: {scores[index]}')

    #create dictionary od names and scores
    student_scores = {
        'Allie': 100,
        'Lincoln': 80,
        'Kian': 54,
        'Joe': 98,
        'Noah': 94,
        'Andrew': 96,
        'Carter': 2,
        'Silas': 87
    }
    #print allie and lincolns scores
    print(student_scores['Allie'])
    print(student_scores['Lincoln'])
    print('\n')
    #get all keys and values from student score dictionary
    for student in student_scores:
        print(f'{student}: {student_scores[student]}')

    #declare car dictionary
    car = {
        'make': 'Porsche', 'model': '911 GT3RS', 'year': 2023, 'value': 330000, 'engine': 4.0, 'horsepower': 502
    }
    #get values from car dictionary
    print('\n')
    for key, value in car.items():
        print(f'{key}: {value}')



main() 