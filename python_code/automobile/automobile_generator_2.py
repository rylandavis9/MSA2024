import automobile as auto
#function load vehichle data from file
#input path to file output list of automobiles
def load_vehicles(file_name):
    #create empty list to store automobile data
    list_of_automobiles = []
    #open file
    auto_file = open(file_name, 'r')

    #ignore the header data row in the filewdddddda
    auto_file.readline()
    #next(auto_file)
    #read each line in for loop
    line_number = 1
    for line_of_data in auto_file:
        #increment line number by 1
        line_number += 1

        #split each line at comma\
        vehicle_data = line_of_data.split(',')

        #check that cehicle_data contains 6 items
        #if not raise error and skip that line of data
        try:
            if len(vehicle_data) != 6:
                raise Exception(f'There is an error in your data file at line {line_number}')
        except Exception as err:
            print(str(err))
            continue

        #get individual values from resulting list
        try:
            make = vehicle_data[0]
            model = vehicle_data[1]
            vin = vehicle_data[2]
            if vehicle_data[3].lower() == 'electric':
                engine_size = 0
            else:
                engine_size = float(vehicle_data[3])
            owner = vehicle_data[4]
            year = int(vehicle_data[5])
        except Exception as err: 
            print(f'Error: {err} on line {line_number}')
            continue

        #create automobile object with data
        new_auto = auto.Automobile(make, model, vin, engine_size, owner, year)
        #append each automobile to the list
        list_of_automobiles.append(new_auto)
    #close file and return the list of automobiles
    auto_file.close()
    return list_of_automobiles

def main():
    #load list of automobiles from data in a file
    automobile_list = load_vehicles('automobile/vehicle_data.csv')

    #print info for each automobile in a for loop
    for vehicle in automobile_list:
        vehicle.print_info()
main()