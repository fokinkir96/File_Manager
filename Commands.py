import os

# DIRECTORY = 'C:/Users/fokin/PycharmProjects/Practicum4sem/FileManager/test/'

'''
TODO:
    1. Команда wrt, отлов текста в кавычках

'''
class Commands:
    '''Класс команд файлового менеджера'''
    def __init__(self, root):
        root = root.replace('\\', '/')
        if root[len(root)-1] == '/':
            root = root[:-1]

        self.ROOT = root
        os.chdir(self.ROOT)
        self.directory = '/'

    def __cmds(self):
        '''Список методов'''
        return [attribute for attribute in dir(self) if callable(getattr(self, attribute)) and attribute.startswith('_') is False]

    def _call(self, cmd):
        '''Вызов команд класса'''
        method_list = self.__cmds()
        if cmd in method_list:
            return self.__getattribute__(cmd)

        return False

    def __make_param(self, dr):
        path = self.ROOT+self.directory+dr

        # if len(dr) == 0:
        #     path = self.directory
        if len(dr) != 0 and dr[0] == '/':
            path = self.ROOT + dr[1:]
        # if path[len(path)-1] != '/':
        #     path += '/'
        # print(path)
        return path

    def sf(self, dr=''):
        '''Показ фалов в папке'''
        return os.listdir(self.__make_param(dr))

    def crtdr(self, dr):
        '''Создание папки'''
        return os.mkdir(self.__make_param(dr))

    def deldr(self, dr):
        '''Удаление папки'''
        return os.rmdir(self.__make_param(dr))

    def chdr(self, dr):
        '''Смена папки'''
        os.chdir(self.__make_param(dr))
        self.directory = os.getcwd().replace('\\', '/')
        print(self.ROOT in self.directory)
        if self.ROOT not in self.directory:
            self.directory = '/'
        else:
            self.directory = self.directory.replace(self.ROOT, '')+'/'
        print(self.directory)

    def crtfl(self, name):
        '''Создание пустого файла'''
        file = open(name, 'w+')
        file.close()

    def wrt(self, name, text):
        '''Запись текста в файл'''
        with open(self.__make_param(name), 'w') as f:
            f.write(text)

    def shfl(self, name):
        '''Вывод содержимого файла'''
        with open(self.__make_param(name), 'r') as f:
            return f.read()

    def delfl(self, name):
        '''Удаление файла'''
        os.remove(self.__make_param(name))

    def cpfl(self, name, copy):
        '''Копирование файла'''
        with open(self.__make_param(name), 'r') as f:
            with open(self.__make_param(copy), 'w') as cp:
                cp.write(f.read())

    def mvfl(self, name, nname):
        '''Перемещение файла'''
        self.rnmfl(name, nname)

    def rnmfl(self, name, nname):
        '''Переименование файла'''
        os.rename(self.__make_param(name), self.__make_param(nname))

    def help(self):
        '''Вывод всех команд'''
        cmds = self.__cmds()
        res = ''
        for cmd in cmds:
            res += cmd+' - '+self.__getattribute__(cmd).__doc__+'\n'

        return res

    def wai(self):
        '''Текущая директория'''
        return self.directory