calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string_1: str):
    count_calls()
    _info = (len(string_1), string_1.upper(), string_1.lower())
    return _info


def  is_contains(string_2: str, list_to_search: list):
    count_calls()
    new_lts = []
    f = True
    for i in range(len(list_to_search)):
        new_lts.append(list_to_search[i].lower())
    # print(new_lts)
    if string_2.lower() in new_lts:
        f = True
    else: f = False
    return f



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)