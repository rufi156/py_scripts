"""
Script to batch rename .mkv and .srt files. Tedious on win10 powershell, easy peasy with python. 
Originaly written in Jupyter notebooks cause thats what I'm currently getting comfortable with.
"""
from pathlib import Path
import os
i=1
# List all files in directory using pathlib
basepath = Path('.')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    if item.name.endswith('.mkv'):
        dst = 'Kimetsu no Yaiba - S01E' + str(i).zfill(2) +'.mkv'
        src = os.path.join('.', item.name)
        dst = os.path.join('.', dst)
        i += 1
        print(item.name)
        #os.rename(src,dst)

#no onto .srt which are not sorted

for number in  range(1,27):
    for entry in os.scandir('.'):
        if entry.is_file():
            if entry.name.endswith(f'({number}).srt'):
                dst = 'Kimetsu no Yaiba - S01E' + str(number).zfill(2) +'.srt'
                src = os.path.join('.', entry.name)
                dst = os.path.join('.', dst)
                print(entry.name)
                #os.rename(src,dst)
