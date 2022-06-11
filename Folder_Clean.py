import os, shutil
from typing import final

folders = [r'C:\Users\UserName\Downloads',
           r'C:\Users\UserName\Documents']

def clean_folder(folder):
    files = []

    # Iterate directory
    for path in os.listdir(folder):
        # check if current path is a file
        if os.path.isfile(os.path.join(folder, path)):
            files.append(path)
    # print(files)

    def get_latest_file(files):

        def split_filename (file):
            return file.split("-")[0]

        def file_version (file):
            return file.split("-")[1].split(".")[0]

        d_file = {}

        for file in files:
            filename = split_filename(file)
            fileversion = file_version(file)
            if filename in d_file:
                d_file[filename].append(fileversion)
            else:
                d_file[filename] = [fileversion]

        final_file = []

        for key in d_file.keys():
            final_file.append(key+"-"+max(d_file[key])+".txt")

        return final_file

    latest_file = get_latest_file(files)

    delete_file = list(set(files) - set(latest_file))

    for filename in delete_file:
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

for folder in folders:
    clean_folder(folder)