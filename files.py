import os
from pathlib import Path

path = Path(r"D:\TestFolder2")

rezerv = ['Archives', 'Documents', 'Else', 'Images', 'Video']

def del_empty_folders(path):
    counter = 0
    global rezerv
    for p, d, f in os.walk(path):
        print(p, d, f, sep='\n')
        print(d == rezerv)
        if (not d ) and (not f) and (d == rezerv):
            os.rmdir(p)
            counter += 1
        if counter > 0:
            del_empty_folders(path)

del_empty_folders(path)