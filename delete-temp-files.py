import os, shutil

def delete_files(dir):
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

delete_files('C:/Windows/Temp')
delete_files('C:/Users/rober/AppData/Local/Temp')
