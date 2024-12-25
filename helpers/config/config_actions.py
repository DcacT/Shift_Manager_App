import os
from dotenv import load_dotenv, set_key, dotenv_values
import json
from datetime import datetime, timedelta
from . import  get_cfg_path, CFG_PATH
roles_list = ['inactive', 'employee', 'manager', 'owner']

Mock_Employee_List = [{
            "NAME": "Steve",
            "DC_ID":"qwer",
            "ROLE": "employee",
            "Desired_Shift_Counts": 3,
            "Priority": 0
        },
        {
            "NAME": "Peter",
            "DC_ID":"asdf",
            "ROLE": "employee",
            "Desired_Shift_Counts": 1,
            "Priority": 0
        },
        {
            "NAME": "Jordan",
            "DC_ID":"zxcv",
            "ROLE": "owner",
            "Desired_Shift_Counts": 3,
            "Priority": 0
        }]
Default_Shift_Pattern = {
    "Employee_Count":"5",
    "Employee1":"10:00-17:00",
    "Employee2":"11:00-18:00",
    "Employee3":"5:00-23:30",
    "Employee4":"5:00-23:30",
    "Employee5":"5:00-23:00",
}

default_employee_base = {
    'NAME': "Steve",
    'DC_ID':'qwer',
    'ROLE': "employee",
    'Desired_Shift_Counts':"0",
    'Priority':'-1' # 0 is standard, -1 is to use as least as possible. max out at 5. 
}
default_values = {
    'BOT_KEY': 'default_api_key',
    'SERVER':'default_server_key',
    'OWNER': 'DISCORD_KEY',
    'OPERATION_TIME':{
        "DAYS":['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        "START_TIME":"10:30", 
        "END_TIME":"23:30",
        "INTERVALS":30, 
        "INTERVALS_COUNT":26, # intervals_count = (datetime.strptime(OPERATION_TIME.END_TIME)-datetime.strptime(OPERATION_TIME.START_TIME)).total_seconds() / 60 //OPERATION_TIME.INTERVALS
    },
    'TIME_SLOT_LIST':[],
    'MANAGER_LIST': [],
    'EMPLOYEE_LIST':Mock_Employee_List,
    'ROLES_LIST':roles_list,
    'SHIFT_PATTERNS':{
        'title':Default_Shift_Pattern
    },
    'WEEKS_PER_SCHEDULE': 1,
    'NEXT_SCHEDULE_DATE':'2024_12_23'
}


def check_cfg():
    get_cfg_path()
    return os.path.exists(CFG_PATH)

def read_cfg(key=None):
    with open(CFG_PATH, 'r') as f:
        data = json.load(f)
    if key is not None and key in data:
        return data[key]
    return data

def write_cfg(key, val):
    with open(CFG_PATH, 'r') as f:
        data = json.load(f)
    
    data[key] = val
    
    with open(CFG_PATH, 'w') as f:
        json.dump(data, f, indent=4)


def setup_cfg(values=default_values, time_slot_list = None):
    if os.path.exists(CFG_PATH): #delete if exist
        os.remove(CFG_PATH)
        print(f"{CFG_PATH} existed and was deleted.")
    
    values['TIME_SLOT_LIST'] = generate_time_slot_list(values) if time_slot_list == None else time_slot_list
    
    with open(CFG_PATH, 'w') as f:
        json.dump(values, f, indent=4)
    print(f"{CFG_PATH} created with default values.")
    
def generate_time_slot_list(data = None):
    OPERATION_TIME = read_cfg(key='OPERATION_TIME') if data == None else data['OPERATION_TIME']
    print(OPERATION_TIME)
    TIME_SLOT_LIST = ['EMPLOYEE']
    for day in OPERATION_TIME['DAYS']:
        if day in ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']:
            for i in range(OPERATION_TIME['INTERVALS_COUNT']):
                start_time = datetime.strptime(OPERATION_TIME['START_TIME'], '%H:%M')
                current_time = start_time + timedelta(minutes=OPERATION_TIME['INTERVALS'] * i)
                cuurent_time_string = datetime.strftime(current_time, '%H:%M')
                TIME_SLOT_LIST.append(f"{day}_{cuurent_time_string}")
    return TIME_SLOT_LIST




