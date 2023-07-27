import os
import shutil

path = "/home/itachidesktop/Downloads"
photos_path = "/home/itachidesktop/Downloads/Photos"

list_dir = os.listdir(path)


def is_photo_file(file_path):
    _, extension = os.path.splitext(file_path)
    if(extension.lower() == '.jpg' or extension.lower() == '.png'):
        shutil.move(file_path, photos_path)
        print('File Move Success')

    else: print('Unknown file')


file_name = 'peakpx.jpg'
full_file_path = os.path.join(path, file_name)
is_photo_file(full_file_path)