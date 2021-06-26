'''
PySync v.0.0.1

by: Shidiq Nur Hidayat (2021)
'''

import os
import shutil
from tqdm import tqdm
import datetime
from tkinter import filedialog
from tkinter import Tk

print("\n==================================")
print(f"          PySync v.0.0.2           ")
print("==================================\n")


def getroot():
    root = Tk()
    root.withdraw()
    root.dirname = filedialog.askdirectory()
    return root.dirname


# source
# sourcepath = "/Users/shidiq/GeNose"
sourcepath = getroot()

# destination
target = "/Volumes/99% VIRUS"

base = os.path.basename(sourcepath)
path_ = os.path.abspath(sourcepath)
folders = [os.path.abspath(f) for f, _, _ in os.walk(path_)]
icopy = 0
for folder in tqdm(folders, total=len(folders), desc='Scanning folders: '):
    list_ = [f for f in os.listdir(folder)]

    for i, item in enumerate(list_):
        try:
            fullpath = os.path.join(folder, item)
            if os.path.isfile(fullpath):
                despath = os.path.join(target, fullpath[fullpath.find(base):])
                if os.path.exists(despath):
                    if os.stat(fullpath).st_mtime - os.stat(despath).st_mtime > 1:
                        shutil.copy2(fullpath, despath)
                        icopy += 1
                else:
                    os.makedirs(os.path.dirname(despath), exist_ok=True)
                    shutil.copy2(fullpath, despath)
                    icopy += 1
        except Exception as ex:
            print(str(ex))
            print(f"File: {item}")


f = open(os.path.join(target, os.path.basename(path_), 'last_sync.txt'), 'a')
f.write(f"Last sync: {datetime.datetime.now()}\n")
f.close()

print("\n==================================")
print(f"Sync update: {icopy} files!")
print("==================================\n")
