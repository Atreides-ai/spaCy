import os
import shutil

KEEP = ('en')


def remove_dirs():
    os.chdir('lang')
    for dir_ in os.listdir(os.getcwd()):
        if os.path.isdir(dir_):
            if dir_ not in KEEP:
                shutil.rmtree(dir_, ignore_errors=False, onerror=None)
    os.chdir('./')


if __name__ == "__main__":
    remove_dirs()