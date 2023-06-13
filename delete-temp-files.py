import os, shutil

def delete_files(dir:str):
    os.chdir(dir)

    dirs = os.listdir()

    print(dirs)

    for directory in dirs:
        try:
            if os.path.isdir(directory):
                shutil.rmtree(directory, ignore_errors=True)
            else:
                os.remove(directory)
        except Exception as e:
            print(e)

temp_paths:list[str] = [
    'C:\\Windows\\Temp',
    os.environ.get('USERPROFILE') + '\\AppData\\Local\\Temp'
]

for path in temp_paths:
    delete_files(path)
