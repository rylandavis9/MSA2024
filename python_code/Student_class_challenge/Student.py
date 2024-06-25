#create a student class
#define a consturcter
#constructor is a function that executes when an object or  is created
class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        #assign class properties values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = float(credit_hours)
        self.__gpa = float(gpa)
        self.__student_id = student_id


    #create get and set methods for class properties
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_first_name):
        #check new_owner is not an empty string
        if new_first_name == '':
            print('ERROR: must enter new name')
            return
        
        self.__first_name = new_first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major
    
    def set_first_name(self, new_major):
        #check new_owner is not an empty string
        if new_major == '':
            print('ERROR: must enter new major')
            return
        
        self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        try:
            self.__credit_hours = float(new_gpa)
        except:
            print('Error: Gpa Must Be A Number\n')
        self.__gpa = new_gpa
    

    def get_student_id(self):
        return self.__student_id
    #get_class_level
    def get_class_level(self):
        class_level = ''
        if self.__credit_hours <= 30:
            class_level = 'Freshman'
        elif self.__credit_hours <= 60:
            class_level = 'Sophomore'
        elif self.__credit_hours <= 90:
            class_level = 'Junior'
        elif self.__credit_hours >= 91:
            class_level = 'Senior'
        return class_level
    
    #UPDATE CREDIT HOURS
    def update_credit_hours(self, hours):
        try:
            self.__credit_hours += float(hours)
        except:
            print('Error: Credit Hours Must Be A Number\n')

    
    #create a method to print student info

    def print_student_data(self):
        class_level = self.get_class_level()
        print(f'{self.__first_name} {self.__last_name} {self.__major}\nCredits: {self.__credit_hours}, GPA: {self.__gpa}\nClass: {class_level}\nStudent ID: {self.__student_id}\n')
        