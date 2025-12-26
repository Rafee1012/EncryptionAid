import subprocess

folders=[]

# runs mkdir in terminal to create folder of name
def make_folder(name):
    subprocess.run("mkdir " + str(name), shell=True) # ISSUE: MAKING FOLDER WITHIN VS CODE, NOT FINDER

def access_folder(name):
    subprocess.run("open .")
    print(name) # OPEN FOLDER WITH NAME FROM FINDER