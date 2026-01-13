import dearpygui.dearpygui as dpg
import os
import sys
sys.path.append('/Users/rafeeahsan/EncryptionAid/EncryptionAid')
from backend.folderManager import make_folder, access_item, folders

screen_dim = {
    "width" : 550,
    "height" : 450,
    "x_pos" : 500,
    "y_pos" : 250
}

def get_input(folder_name, tag):
    captured_item = dpg.get_value(folder_name)
    dpg.delete_item(tag)
    return captured_item

# adds new window to create folder
def create_folder():
    with dpg.window(tag= "create_subwindow",
                    label="Create Folder",
                    width=screen_dim["width"]/1.5,
                    height=screen_dim["height"]/4.5,
                    pos=[90, 200]):
        dpg.add_text("Enter folder name:", pos=[22, 30])
        dpg.add_input_text(tag="FOLDER_INPUT_FOR_CREATE", hint="Add Name",
                                        width=250,
                                        pos=[20, 55])
        dpg.add_button(label="Confirm", callback=lambda: make_folder(get_input("FOLDER_INPUT_FOR_CREATE", "create_subwindow")),
                                        pos=[285, 55])
    
# opens previously created folder
def open_folder():
    with dpg.window(tag= "open_subwindow",
                    label="Create Folder",
                    width=screen_dim["width"]/1.5,
                    height=screen_dim["height"]/4.5,
                    pos=[90, 200]):
        dpg.add_text("Enter folder name:", pos=[22, 30])
        dpg.add_input_text(tag="FOLDER_INPUT_FOR_OPEN", hint="Find Folder",
                                        width=250,
                                        pos=[20, 55])
        dpg.add_button(label="Confirm", callback=lambda: access_item(get_input("FOLDER_INPUT_FOR_OPEN", "open_subwindow")),
                                        pos=[285, 55])
    # access terminal and use open folder_name to open folder
    print()

def run_app():
    ## Main script must create context and viewport
    dpg.create_context()
    dpg.create_viewport(title='EncryptionAid',
                        width=screen_dim["width"],
                        height=screen_dim["height"],
                        x_pos=screen_dim["x_pos"],
                        y_pos=screen_dim["y_pos"])

    with dpg.window(tag="Primary Window"):
        dpg.add_text("Welcome")
        dpg.add_button(label="Create Folder", pos=[150, screen_dim["y_pos"]/2],
                        callback=create_folder)
        dpg.add_button(label="Access Folder", pos=[300, screen_dim["y_pos"]/2],
                        callback=open_folder)
        #dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    ## Main script must setup gui, show viewport, start gui, and destroy context
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

'''
1.
2.
3.
4.
5.
'''

'''
Create visual chart of file paths as items are added
Add 'add file' button.
Encrypt added files.
?? Add 'create file' button with document editor.
Make EAroot invisible
'''