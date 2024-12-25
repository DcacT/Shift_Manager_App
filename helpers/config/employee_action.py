from ..config import config_actions 

default_employee_base = {
    'NAME': "-", # display name
    'DC_ID': '-',
    'ROLE': "employee",
    'DESIRED_SHIFT_COUNT':"0",
    'PRIORITY':'-1' # 0 is standard, -1 is to use as least as possible. max out at 5. 
}

def show_employee(name = None):
    EMPLOYEE_LIST = config_actions.read_cfg(key = 'EMPLOYEE_LIST')
    if name == None:
        print('EMPLOYEE_LIST', EMPLOYEE_LIST)
        return EMPLOYEE_LIST
    else:
        employee = next((e for e in EMPLOYEE_LIST if e["NAME"] == name), None)
        print('EMPLOYEE: ', employee)
        return employee
    
def create_employee(employee):
    EMPLOYEE_LIST = config_actions.read_cfg(key = 'EMPLOYEE_LIST')
    employee_name = employee['NAME']
    existing_employee_names = [e['NAME'] for e in EMPLOYEE_LIST]
    if employee_name not in existing_employee_names:
        EMPLOYEE_LIST.append(employee)
        config_actions.write_cfg(key='EMPLOYEE_LIST', val=EMPLOYEE_LIST)
        print('employee created! ')
        show_employee()
    else: 
        print('employee name invalid! repeated!')
        show_employee()
    return

def delete_employee(NAME = None, DC_ID = None):
    EMPLOYEE_LIST = config_actions.read_cfg(key = 'EMPLOYEE_LIST')
    if NAME is not None:
        index, employee = next(((i, e) for i, e in enumerate(EMPLOYEE_LIST) if e["NAME"] == NAME), None)
        if employee is not None:
            del EMPLOYEE_LIST[index]
            config_actions.write_cfg(key='EMPLOYEE_LIST', val=EMPLOYEE_LIST)
            print('employee deleted! ')
            show_employee()
            return True
        else:
            print('No employee found with name: ', NAME)
    if DC_ID is not None:
        index, employee = next(((i, e) for i, e in enumerate(EMPLOYEE_LIST) if e["DC_ID"] == DC_ID), None)
        if employee is not None:
            del EMPLOYEE_LIST[index]
            config_actions.write_cfg(key='EMPLOYEE_LIST', val=EMPLOYEE_LIST)
            print('employee deleted! ')
            show_employee()
            return True
        else:
            print('No employee found with ID: ', DC_ID)
            return False
    print('Employee Name or DC_ID cannot be empty')
    return False


default_employee_base = {
    'NAME': "-", # display name
    'DC_ID': '-',
    'ROLE': "employee",
    'DESIRED_SHIFT_COUNT':"0",
    'PRIORITY':'-1' # 0 is standard, -1 is to use as least as possible. max out at 5. 
}


def edit_employee(name, key, val):
    EMPLOYEE_LIST = config_actions.read_cfg(key = 'EMPLOYEE_LIST')
    index, employee = next(((i, e) for i, e in enumerate(EMPLOYEE_LIST) if e["NAME"] == name), None)
    
    if key == 'PRIORITY': # check value in range
        if not (-1 <= val <= 5) or not isinstance(val, int):
            #discord prompt sth 
            print('PRIORITY VALUE OUT OF RANGE (-1<=n<=5) OR NOT INTEGER')
        else:
            employee['PRIORITY'] = val

    elif key == 'NAME': # check for duplicates
        existing_employee = next((e for e in EMPLOYEE_LIST if e["NAME"] == val), None)
        if existing_employee != None:
            print('existing name exist!')
        else:
            employee['NAME'] = val

    elif key == 'DC_ID':
        employee['DC_ID'] = val

    elif key == 'DESIRED_SHIFT_COUNT':
        if val <-1:
            print('less than minimum(-1)')
        else:
            employee['DESIRED_SHIFT_COUNT'] = val
    else:
        print('unrecognized attribute: ', key)
        return
    EMPLOYEE_LIST[index] = employee
    config_actions.write_cfg(key='EMPLOYEE_LIST', val=EMPLOYEE_LIST)
    print('employee editted: ', employee)
    show_employee()

    