import datetime
from . import config_actions

def get_last_date(): #TODO
    return None
    
def generate_file_name(file_type = 'AVAILABILITY', start_date = None, folder_path = None):
    
    WEEKS_PER_SCHEDULE = config_actions.read_cfg('WEEKS_PER_SCHEDULE')
    if start_date is None:
        get_last_date()
    else:
        start_date = datetime.datetime.now().strftime('%y_%m_%d')
    file_name = file_type + '_' + start_date 
    return file_name


