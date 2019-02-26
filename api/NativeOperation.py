import shutil
import subprocess, os
import sys
from os.path import isfile


def open_file_locally(filepath):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))
    elif os.name == 'nt':  # For Windows
        os.startfile(filepath)
    elif os.name == 'posix':  # For Linux, Mac, etc.
        subprocess.call(('xdg-open', filepath))


def show_in_exploror(filepath):
    print("filepath", filepath)
    print("filepath", filepath.replace(" ", "^ "))
    subprocess.Popen(r'explorer /select,' + filepath)


def move_file(source, destination):
    if isfile(source):
        shutil.move(source, destination)
