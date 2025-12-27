import os
import subprocess

folders=[]

# requires file system to have a Documents folder
# initialise program, create app root folder if needed
def init_app():
    name = os.environ.get("USER")
    root_string = 'mkdir /Users/' + name + '/Documents/EAroot'
    subprocess.run(root_string, shell=True)

# requires file system to have a Documents folder
# runs mkdir in terminal to create folder of name
def make_folder(name):
    folder_path_string = 'mkdir /Users/' + name + '/Documents/EAroot' + str(name)
    subprocess.run(folder_path_string, shell=True)

def access_folder(name):
    subprocess.run('open .')
    print(name) # OPEN FOLDER WITH NAME FROM FINDER