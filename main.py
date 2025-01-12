import os
from .helpers.config import config_actions, employee_action
from .helpers.csv import availability_actions, visualizer

def onStart():
    # config_actions.setup_cfg()
    print(visualizer.get_list_of_days())
    data = availability_actions.generate_empty_availability_data(start_from_scratch=True)
    # availability_actions.write_availability_data(data, 'new_sample.csv')


    data =visualizer.split_csv_with_days()
    print(data[1])
    df = visualizer.list_to_df(data[2])
    df = visualizer.display_df(df = df)
    visualizer.save_df_to_html(df)

def get_integer(prompt="Enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
#config_handler

def availability_handler():
    NEXT_SCHEDULE_DATE = config_actions.read_cfg('NEXT_SCHEDULE_DATE')
    command = input(f'Availability command ({NEXT_SCHEDULE_DATE}): ')
    
    if command == 'show':
        list_of_days = visualizer.get_list_of_days()
        for i, day in enumerate(list_of_days):
            print(f'{i}: {day}')
        which_day = input('which day? "all" for all: ')
        if which_day != 'all' or which_day<0 or which_day >= len(list_of_days):
            print('error input')
            return 

        data =visualizer.split_csv_with_days()
        print_data = data if which_day == 'all' else data[which_day]
        show_what = input('Show What: ')
        if show_what == 'raw':     
            print(print_data)
        elif show_what == 'table':
            df = visualizer.list_to_df(print_data)
            df = visualizer.display_df(df = df)
            visualizer.save_df_to_html(df)#shift_handler
    elif command == 'edit':
        which_person = input('which person: ')
        
        list_of_days = visualizer.get_list_of_days()
        for i, day in enumerate(list_of_days):
            print(f'{i}: {day}')
        which_day = input('which day: ')
        if type(which_day) is not int or which_day<0 or which_day >= len(list_of_days):
            print('error input')
            return 
        
        which_status = input('which status(O/X): ')
        if which_status is not 'O' and which_status is not 'X':
            print('invalid status')   

        TIME_SLOST_LIST = config_actions.read_cfg('TIME_SLOT_LIST')
        for i, time_slot in TIME_SLOST_LIST:
            print(f'{i}: {time_slot}')
        which_start_time = input('which start_time: ')
        if which_start_time < 0: 
            print('invalid start time')
        which_end_time = input('which end time')
        
#employee_handler
default_employee_base = {
    'NAME': "Steve",
    'DC_ID':'qwer',
    'ROLE': "employee",
    'Desired_Shift_Counts':"0",
    'Priority':'-1' # 0 is standard, -1 is to use as least as possible. max out at 5. 
}
def handle_employee():
    command = input('Employee command: ')
    if command == 'show':
        employee_action.show_employee()
    elif command == 'new':
        ok = False
        while not ok:
            name = input('Name of employee: ')
            list_of_roles = config_actions.read_cfg('ROLES_LIST')
            
            print('ROLES_LIST')
            for role in list_of_roles:
                print(role)
            role = ''
            while role == '': 
                r = input('role:')
                if r not in list_of_roles:
                    print('invalid roles')
                else:
                    role = r
            
            while True:
                try:
                    shift_count = int(input("Desired Shifts Count Per Week: "))
                    break
                except ValueError:
                    print("That's not an integer. Try again.")

            DC_ID = input('Discord ID: ')
            priority = 0
          
            new_employee = {
                'NAME': name,
                'DC_ID':DC_ID,
                'ROLE': role,
                'Desired_Shift_Counts':shift_count,
                'Priority':priority # 0 is standard, -1 is to use as least as possible. max out at 5. 
            }
            print (new_employee)
            ok = input('ok?') == 'ok'
        employee_action.create_employee(new_employee)
    elif command == 'delete':
        employee_action.delete_employee(NAME = input('Delete Employee Name: '))
        return
    elif command == 'edit':

        return  
    else: 
        print('unrecognized availability command')


##########   COMANDS   ###########
def handle_commands():
    try:
        while True:
            command = input("Enter command: ")
            if command.startswith("!help"):
                print("!help")
            elif command.startswith("!reset"):
                print("reset everything")
                config_actions.setup_cfg()

            elif command.startswith("!config"):
                1

            elif command.startswith("!availability"):
                handle_employee()
            
            elif command.startswith("!shift"):
                handle_employee()
            
            elif command.startswith("!employee"):
                handle_employee()

            else:
                print("Unknown command")
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    onStart()
    handle_commands()