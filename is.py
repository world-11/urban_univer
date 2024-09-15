import sys, inspect


def introspection_info(obj):
    # help(sport)
    info = {}
    info['тип обьекта'] = type(obj)
    info['описание класса'] = inspect.getcomments(obj)
    info['атрибуты'] = inspect.getmembers(obj, lambda attr: not (inspect.isroutine(attr)))
    info['методы'] = inspect.getmembers(obj, inspect.isroutine)
    info['функции'] = inspect.getmembers(obj, inspect.isfunction)
    info['модуль'] = inspect.getmodule(obj)
    info['версия python'] = sys.version
    info['версия os'] = sys.platform
    info['interpretator'] = sys.executable
    info['path поиска модуля'] = sys.path
    return info


# импровизированный тип данных
class sport(object):

    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    # тип движения
    def moving(self):
        self.V = 10
        g = 10
        def run():
            pass
        def swim():
            pass
        def cicle():
            pass
        def restling():
            pass

    # материальная база
    def mat_base(self):
        money = 100000
        gym = True
        cort = True
        forest_circle = True

    # чемпионаты
    @classmethod
    def cup(self):
        cup_ = 100 * self.V
        return cup_

boy = sport(12321, 'Ivanov', 15, )
a = introspection_info(boy)
for key in a:
        print(f'{key}: {a[key]}')