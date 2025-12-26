import dearpygui.dearpygui as dpg
import sys
sys.path.append('/Users/rafeeahsan/EncryptionAid/EncryptionAid')
from backend.folderManager import make_folder, access_folder, folders

screen_dim = {
    "width" : 550,
    "height" : 450,
    "x_pos" : 500,
    "y_pos" : 250
}

# adds new window to create folder
def create_folder():
    with dpg.window(label="Create Folder",
                    width=screen_dim["width"]/1.5,
                    height=screen_dim["height"]/4.5,
                    pos=[90, 200]):
        dpg.add_text("Enter folder name:", pos=[20, 30])
        folder_name = dpg.add_input_text(label="",
                                        pos=[20, 55])
        dpg.add_button(label="Confirm", callback=make_folder(folder_name),
                                        pos=[285, 55])
        folders.append(folder_name)

# opens previously created folder
def open_folder():
    with dpg.window():
        dpg.add_button(label="Confirm", callback=access_folder("NAME")) # ALLOW USE TO CHOOSE SPECIFIC FILE FROM THIS PROGRAM, OPEN IT AND REPLACE 'NAME'
    # access terminal and use open folder_name to open folder
    print()

def main():
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

if __name__ == "__main__":
    main()
