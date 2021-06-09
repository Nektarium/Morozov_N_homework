# модуль easy

import os
from shutil import copyfile


def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), '{0}'.format(dir_name))
    try:
        os.mkdir(dir_path)
        print("\nДиректрия {0} создана".format(dir_name))
    except FileExistsError:
        print("\nДиректория {0} уже существует")


def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), '{0}'.format(dir_name))
    try:
        os.rmdir(dir_path)
        print("\nДиректрия {0} удалена".format(dir_name))
    except FileNotFoundError:
        print("\nДиректория {0} не существует".format(dir_name))


def list_dir():
    print("Папки текущей директории:")
    for item in (list(i for i in os.listdir(path=os.getcwd()) if os.path.isdir(i))):
        print(item)


def copy():
    copy_filename = __file__ + " (копия)"
    copyfile(__file__, copy_filename)

def change_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), '{0}'.format(dir_name))
    try:
        os.chdir(dir_path)
        print("\nВы успешно сменили текущую директорию: ", dir_path)
    except FileNotFoundError:
        print('\nТакая директория не существует')
