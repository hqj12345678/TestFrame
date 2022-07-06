import os
from config import  setting
def new_report(path):
    dirs=os.listdir(path)
    dirs.sort(key=lambda fn: os.path.getmtime(path + "/" + fn))
    filepath=os.path.join(path,dirs[-1])
    return filepath
