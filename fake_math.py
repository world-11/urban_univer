def fake_divide (first, second):
    res = 1.0
    if second == 0:
        res = 'Ошибка!'
    else:
        res = first / second
    return res