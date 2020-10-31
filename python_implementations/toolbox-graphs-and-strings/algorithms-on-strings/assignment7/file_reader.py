import os
import glob


def read_multiple_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    
    return files