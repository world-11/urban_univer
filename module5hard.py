import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title: str, duration: time = 0, time_now: time = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user: User = None

    def log_in(self, nickname: str, password: str):
        if self.current_user != None:
            for y in self.users:
                if y.nickname == nickname and y.password == hash(password):
                    self.current_user = y
                    break
                else:
                    print('Пользователь с таким именем/паролем не зарегистрирован')
                    break

    def log_out(self):
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        y = User(nickname = nickname, password = password, age = age)
        f = False #наличие юзера в списке
        for x in self.users:
            if x.nickname == y.nickname:
                f = True
                break
        if f == True:
            return print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(y)
            self.current_user = y

    def add(self, *args: Video):
        for x in args:
            if x.title in self.videos:
                print('Видео с таким названием уже есть')
            else:
                self.videos.append(x)

    def get_videos(self, sw: str):
        result = []
        n_sw = sw.lower()
        f = False
        for x in self.videos:
            x1 = x.title.lower()
            if n_sw in x1:
                result.append(x.title)
        if result == []:
            f = True and print("Такого видео нет")
        return result

    def handler(signum, frame):
        print('Signal handler called with signal', signum)
        exit()

    def watch_video(self, video_title: str):
        f = True
        if self.current_user != None:
            # if s in self.videos:
            #     print('Такого видео нет')
            #     return
            for y in self.videos:
                if y.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    if video_title == y.title:
                        f = False
                        for i in range(y.duration):
                            print (i, end="")
                            time.sleep(1)
                            print( end='\r')
                        print("\r", end="")
                        print("Конец видео")
                        break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if f == True:
            print('Такого видео нет')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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