import csv
from ..config import config_actions
from datetime import timedelta, datetime
import os
dir_path = os.path.dirname(__file__)


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
def get_next_availability_sheet_name():
    date_str = config_actions.read_cfg('NEXT_SCHEDULE_DATE')
    return os.path.join(dir_path, f"AVAILABILITY_{date_str}.csv")

def get_this_availability_sheet_name():
    date_str = config_actions.read_cfg('NEXT_SCHEDULE_DATE')
    new_date_str = (datetime.strptime(date_str, f"%Y_%m_%d") - timedelta(days=7)).strftime(f"%Y_%m_%d")
    return os.path.join(dir_path, f"AVAILABILITY_{new_date_str}.csv")



def generate_empty_availability_data(start_from_scratch = False):
    # read configuration
    print('GENERATING AVAILABILITY DATA')
    TIME_SLOT_LIST = config_actions.read_cfg(key='TIME_SLOT_LIST')
    EMPLOYEE_LIST = config_actions.read_cfg(key='EMPLOYEE_LIST')
    # generate column list

    AVAILABILITY_DATA = [TIME_SLOT_LIST[0]] + EMPLOYEE_LIST
    print(AVAILABILITY_DATA)
    for t in TIME_SLOT_LIST[1:]:
        ROW = [t]
        
        for person in EMPLOYEE_LIST:
            if start_from_scratch:
                ROW.append('O')
            else:
                print('TODO')
        AVAILABILITY_DATA.append(ROW)
    # print(AVAILABILITY_DATA)
    return AVAILABILITY_DATA               

def write_availability_data(data, file_name=None):
    
    file_name = get_next_availability_sheet_name() if file_name == None else file_name
    # file_name = util.generate_file_name()
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def read_availability_data(data, file_name = None):
    file_name = get_next_availability_sheet_name() if file_name == None else file_name
    # file_name = util.generate_file_name()
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

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

# TODO make TIME_SLOT_LIST in config 

def range_modify_availability_data(data, employee_index, start_time_index, end_time_index, availability = False, employee_name = None, start_time_name = None, end_time_name = None):
    
    if employee_index == None and employee_name != None:
        employee_index = get_employee_index(employee_name)
    if start_time_index == None and start_time_name != None:
        start_time_index = get_time_index(start_time_name)  
    if end_time_index == None and end_time_name != None:
        end_time_index= get_time_index(end_time_index)  
        
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
    
