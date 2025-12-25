import subprocess

folders=[]

def make_folder(name):
    subprocess.run("mkdir " + name, shell=True)