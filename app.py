import os
import shutil
import time

path = "/home/itachidesktop/Downloads"
photos_path = "/home/itachidesktop/Downloads/Photos"



def is_photo_file(file_path):
    _, extension = os.path.splitext(file_path)
    if(extension.lower() == '.jpg' or extension.lower() == '.png' or extension.lower() == '.jpeg'):
        shutil.move(file_path, photos_path)
        print('File Move Success')

    else: print('Unknown file')


while True:
    list_dir = os.listdir(path)

    for file in list_dir:
        full_file_path = os.path.join(path, file)
        is_photo_file(full_file_path)

    time.sleep(10)