import Student as student
from datetime import datetime
'''
function to write error log file
Input Error message
output none
'''
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open('student_data_api\error_log.txt', 'a')
        #write error message
        log_file.write(f'{datetime.now()}: {error_message}\n')
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
    return

#function load studente data from file
#input path to file output list of students
def load_students(file_name):
    #create empty list to store student data
    list_of_students = []
    #open file
    student_file = open(file_name, 'r')

    #ignore the header data row in the filewdddddda
    student_file.readline()
    #next(student_file)
    #read each line in for loop
    line_number = 1
    for line_of_data in student_file:
        #increment line number by 1
        line_number += 1

        #split each line at comma\
        student_data = line_of_data.split(',')

        #check that student_data contains 6 items
        #if not raise error and skip that line of data
        try:
            if len(student_data) != 6:
                raise Exception(f'There is an error in your data file at line {line_number}')
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get individual values from resulting list
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_id = student_data[5]

        except Exception as err: 
            write_to_error_log(f'Error: {err} on line {line_number}')
            continue

        #create student object with data
        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
        #append each student to the list
        list_of_students.append(new_student)
    #close file and return the list of students
    student_file.close()
    return list_of_students

#create function called student to dictionary that creates a student dictionary for each student object
#add student dictionary to a list
#function to create a list of student dictionaries
#input list of student objects
#output list of student dictionaries
def student_to_dictionary(list_of_students):
    #loop through the list of students with a for loop
    list_of_student_dictionaries = []
    #create dictionary for each student object
    for item in list_of_students:
        student_dictionary = {
            'first_name': item.get_first_name(),
            'last_name': item.get_last_name(),
            'id': item.get_student_id(),
            'major': item.get_major(),
            'gpa': item.get_gpa(),
            'class': item.get_class_level()
        }
        #append the student dictionary to the list of dictionaries
        list_of_student_dictionaries.append(student_dictionary)

    return list_of_student_dictionaries
    


def get_student_dictionaries():
    #load list of students from data in a file
    
    list_of_students = load_students('student_data_api\students.csv')

    student_dictionary = student_to_dictionary(list_of_students)

    return student_dictionary

get_student_dictionaries()