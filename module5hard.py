import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title: str, duration: int = 0, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user: []



    # какое критическое количество итераций должно быть
    def log_in(self, nickname: str, password: str):
            for user_search in self.users:
                if user_search.nickname == nickname and user_search.password == hash(password):
                    self.current_user = user_search
                    break
                else:
                    print('Пользователь с таким именем/паролем не зарегистрирован')
                    break

    def log_out(self):
        self.current_user = []  #как заменить данную строрку?

    def register(self, nickname: str, password: str, age: int):
        new_user = User(nickname = nickname, password = password, age = age)
        f = False #наличие юзера в списке
        for x in self.users:
            if x.nickname == new_user.nickname:
                return print(f'Пользователь {nickname} уже существует')
        self.users.append(new_user)
        self.current_user = new_user

    def add(self, *args):
        for x in args:
            if self.videos != []:
                for v in self.videos:
                    if x.title == v.title:
                        return print(f'Видео {x.title} уже существует')
                    else:
                        self.videos.append(x)
            else:
                self.videos.append(x)

    def get_videos(self, need_video: str):
        result = []
        for x in self.videos:
            if need_video.lower() in x.title.lower():
                result.append(x.title)
        if result == []:
            print("Видео с таким названием нет")
        return result

    def watch_video(self, video_title: str):
        f = True #отсутствие видео в списке
        if self.current_user != []:
            for video_ in self.videos:
                if video_.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    if video_title == video_.title:
                        f = False
                        for i in range(video_.duration):
                            print (i, end="")
                            self.time_now = i
                            time.sleep(1)
                            print( end='\r')
                        print("\r", end="")
                        print("Конец видео")
                        self.time_now = 0
                        break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if f == True: #отсутсвие видео
            print('Такого видео нет')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)#

# Добавление видео
ur.add(v1, v2, v3)# не проверяет

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

ur.log_in('Nikolay', 'qwerty')
print(ur.current_user.nickname)

ur.register('Nikolay', 'qwerty', 35)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')