def is_prime(function):

    def wrapper(*kwargs):
        a = function(*kwargs)
        flag = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                flag += 1
        if flag == 0:
            print('Простое')
            return a
        else:
            print('Составное')
            return a
    return wrapper


@is_prime
def sum_three(a:int, b:int, c:int):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)