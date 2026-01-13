import os
import subprocess

folders=[]
name = os.environ.get("USER")

# requires file system to have a Documents folder
# initialise program, create app root folder if needed
def init_app():
    root_string = 'mkdir /Users/' + name + '/Documents/EAroot'
    subprocess.run(root_string, shell=True)

# requires file system to have a Documents folder
# runs mkdir in terminal to create folder of name
def make_folder(item_name):
    if (item_name == ''):
        print("Cannot create empty folder.") #TODO: write to program interface
        return
    folder_path_string = 'mkdir /Users/' + name + '/Documents/EAroot/' + str(item_name)
    subprocess.run(folder_path_string, shell=True)
    folders.append(item_name)
    print(folders)

def access_item(item_name):
    if (item_name == "EAroot"):
        subprocess.run('open /Users/' + name + '/Documents/EAroot')
        return
    elif (item_name == ""):
        print("Cannot create empty folder.") #TODO: write to program interface
        return
    folder_path_string = 'open /Users/' + name + '/Documents/EAroot/' + str(item_name)
    subprocess.run(folder_path_string, shell=True)

# from https://coderivers.org/blog/check-if-folder-exists-python/
# checks if root folder of the program is already in Finder, returns boolean
def hasRootFolder():
    folder_path = 'Documents/EAroot'
    return os.path.exists(folder_path)