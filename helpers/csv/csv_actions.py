import csv
from ..config import config_actions
from datetime import timedelta, datetime


def read_csv_to_list(file_path):

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]  # Store all rows in a list
    return data


# sample OPERATION_TIME:
    # 'OPERATION_TIME':{
    #     'DAYS':['MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY'],
    #     'START_TIME':'10:30', 
    #     'END_TIME':'23:30',
    #     'INTERVALS':'30', 
    #     'INTERVALS_COUNT':'26' # intervals_count = (datetime.strptime(OPERATION_TIME.END_TIME)-datetime.strptime(OPERATION_TIME.START_TIME)).total_seconds() / 60 //OPERATION_TIME.INTERVALS
    # },

def generate_empty_availability_data(start_from_scratch = False):
    # read configuration
    print('GENERATING AVAILABILITY DATA')
    OPERATION_TIME = config_actions.read_cfg(key='OPERATION_TIME')
    EMPLOYEE_LIST = config_actions.read_cfg(key='EMPLOYEE_LIST')
    # generate column list
    COLUMN = ['EMPLOYEE']
    for day in OPERATION_TIME['DAYS']:
        if day in ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']:
            for i in range(OPERATION_TIME['INTERVALS_COUNT']):
                start_time = datetime.strptime(OPERATION_TIME['START_TIME'], '%H:%M')
                current_time = start_time + timedelta(minutes=OPERATION_TIME['INTERVALS'] * i)
                cuurent_time_string = datetime.strftime(current_time, '%H:%M')
                COLUMN.append(f"{day}_{cuurent_time_string}")
    AVAILABILITY_DATA = []
    for t in COLUMN:
        ROW = [t]
        
        for person in EMPLOYEE_LIST:
            if t[0:3] == 'EMP':    
                ROW.append(person)
            else:    
                if start_from_scratch:
                    ROW.append('O')
        AVAILABILITY_DATA.append(ROW)
    print(AVAILABILITY_DATA)
    return AVAILABILITY_DATA               

def write_availability_data(data, file_name):
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def get_employee_index(employee_name):
    EMPLOYEE_LIST = config_actions.read_cfg(key='EMPLOYEE_LIST')
    employee_index = EMPLOYEE_LIST.index(employee_name)
    return employee_index + 1

def get_time_index(data, day, time):
    time_title = f"{day}_{time}"
    column_one = [row[0] for row in data]
    time_index = column_one.index(time_title)
    return  time_index

def modify_availability_data (data, employee_index, time_index, availability = False):
    data[time_index][employee_index] = availability

    return data

def range_modify_availability_data(data, employee_index, start_time_index, end_time_index, availability = False):
    while start_time_index<=end_time_index:
        modify_availability_data(data=data, employee_index=employee_index, time_index=start_time_index, availability=availability)
        start_time_index+=1
    return data


# def setup_cfg(values=default_values):
#     if os.path.exists(CFG_PATH): #delete if exist
#         os.remove(CFG_PATH)
#         print(f"{CFG_PATH} existed and was deleted.")
    
#     with open(CFG_PATH, 'w') as f:
#         json.dump(default_values, f, indent=4)
#     print(f"{CFG_PATH} created with default values.")
    
