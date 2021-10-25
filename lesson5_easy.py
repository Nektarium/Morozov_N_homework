import os
from shutil import copyfile

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

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

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    print("Папки текущей директории:")
    for item in (list(i for i in os.listdir(path=os.getcwd()) if os.path.isdir(i))):
        print(item)


list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy():
    copy_filename = __file__ + " (копия)"
    copyfile(__file__, copy_filename)


copy()
