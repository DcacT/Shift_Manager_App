import pandas as pd
import os 
from ..csv import availability_actions
import imgkit
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def color_cells(val):
    
    if val == 'O':
        return "background-color: red; color: white;"
    elif val == 'X':
        return "background-color: yellow; color: black;"
    else:
        return "background-color: green; color: white;"
    
def read_CSV():
    file_path = availability_actions.get_next_availability_sheet_name()
    return pd.read_csv(file_path)
def display_df():
    df = read_CSV()
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
