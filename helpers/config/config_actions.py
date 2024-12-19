import os
from dotenv import load_dotenv, set_key, dotenv_values
import json
from . import  get_cfg_path, CFG_PATH
roles_list = ['inactive', 'employee', 'manager', 'owner']

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
    'ROLE': "employee",
    'Desired_Shift_Counts':"0"
    
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
    'MANAGER_LIST': [],
    'EMPLOYEE_LIST':['Steve', 'Steven'],
    'roles':roles_list,
    'Shift_Patterns':{
        'title':Default_Shift_Pattern
    },
    'WEEKS_PER_SCHEDULE': 1,

}


def check_cfg():
    get_cfg_path()
    return os.path.exists(CFG_PATH)

def read_cfg(key=None):
    with open(CFG_PATH, 'r') as f:
        data = json.load(f)

    if key and key in data:
        return data[key]
    return data

def write_cfg(key, val):
    with open(CFG_PATH, 'r') as f:
        data = json.load(f)
    
    data[key] = val
    
    with open(CFG_PATH, 'w') as f:
        json.dump(data, f, indent=4)


def setup_cfg(values=default_values):
    if os.path.exists(CFG_PATH): #delete if exist
        os.remove(CFG_PATH)
        print(f"{CFG_PATH} existed and was deleted.")
    
    with open(CFG_PATH, 'w') as f:
        json.dump(default_values, f, indent=4)
    print(f"{CFG_PATH} created with default values.")
    




