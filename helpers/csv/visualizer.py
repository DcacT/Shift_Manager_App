import pandas as pd
import os 
from ..csv import availability_actions
import imgkit
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ..config import config_actions
import numpy as np
def color_cells(val):
    
    if val == 'O':
        return "background-color: red; color: white;"
    elif val == 'X':
        return "background-color: yellow; color: black;"
    else:
        return "background-color: green; color: white;"

def get_list_of_days():
    TIME_SLOT_LIST = config_actions.read_cfg('TIME_SLOT_LIST')[1:]
    b = [A[:3] for i, A in enumerate(TIME_SLOT_LIST) if i == 0 or A[:3] != TIME_SLOT_LIST[i-1][:3]]
    return b

def read_availability_CSV_2_PD():
    file_path = availability_actions.get_next_availability_sheet_name()
    return pd.read_csv(file_path)

def read_availability_CSV_2_NP():
    file_path = availability_actions.get_next_availability_sheet_name()
    
    return np.genfromtxt(file_path, delimiter=",", dtype=str)

def split_csv_with_days():
    data = read_availability_CSV_2_NP()
    print(data)
    
    list_of_days = get_list_of_days()
    day_index = 0
    NEXT_SCHEDULE_DATE = config_actions.read_cfg("NEXT_SCHEDULE_DATE")
    row_header = data[0]
    new_row_header = [NEXT_SCHEDULE_DATE] + (row_header[1:].tolist())

    print('new row header', new_row_header)
    split_datas = [[new_row_header]]
    
    for row in data[1:]:
        row_header = row[0][0:3]
        # print(i,': ',day_index)
        # print(row_header, '; ', list_of_days[day_index])
        if  row_header != list_of_days[day_index]:
            day_index += 1
            split_datas.append([new_row_header])
        
        split_datas[day_index].append(row.tolist())
    
    return split_datas

def list_to_df(data = None):
    return pd.DataFrame(data[1:], columns=data[0]) if data is not None else None

def display_df(df = None):
    df = read_availability_CSV_2_PD() if df is None else df
    styled_df = df.style.applymap(color_cells)
    return styled_df

def save_df_to_html(df):
    html_file = os.path.join(os.path.dirname(__file__), 'd.html')
    df.to_html(html_file)
    
    png_file = os.path.join(os.path.dirname(__file__), 'd.png')
    imgkit.from_file(html_file, png_file)

    img = mpimg.imread(png_file)
    plt.imshow(img)
    plt.axis('off')  # Hide axes for better display
    plt.show()
