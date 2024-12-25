import os
from .helpers.config import config_actions, employee_action
from .helpers.csv import availability_actions

def onStart():
    config_actions.setup_cfg()
    data = availability_actions.generate_empty_availability_data(start_from_scratch=True)
    availability_actions.write_availability_data(data, 'new_sample.csv')

#config_handler

#availability_handler


#shift_handler

#employee_handler
default_employee_base = {
    'NAME': "Steve",
    'ROLE': "employee",
    'Desired_Shift_Counts':"0",
    'Priority':'-1' # 0 is standard, -1 is to use as least as possible. max out at 5. 
}
def handle_employee():
    command = input('Employee command?')
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
                    shift_count = int(input("Desired Shifts Count Per Week : "))
                    break
                except ValueError:
                    print("That's not an integer. Try again.")

            priority = 0
         
            new_employee = {
                'NAME': name,
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
            
            elif command.startswith("!Employee"):
                handle_employee()

            else:
                print("Unknown command")
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    onStart()
    handle_commands()