from random import randint

_game_combination = []
_user_combination = []
_result = {'bulls': 0, 'cows': 0}


def get_a_combination():
    global _game_combination
    _game_combination = []
    _first_iteration = True
    while len(_game_combination) < 4:
        start = 0 if not _first_iteration else 1
        _random_number = randint(start, 9)
        if _random_number not in _game_combination:
            _game_combination.append(_random_number)
            _first_iteration = False
    return _game_combination


def input_number(user_input):
    global _user_combination
    _user_combination = user_input
    _user_combination = [int(item) for item in _user_combination]


def check_number():
    _bulls_count = 0
    _cows_count = 0
    for i in range(0, 4):
        _game_number = _game_combination[i]
        _user_number = _user_combination[i]
        if _game_number == _user_number:
            _bulls_count += 1
    for item in _user_combination:
        if item in _game_combination:
            _cows_count += 1
    _cows_count -= _bulls_count
    global _result
    _result['bulls'] = _bulls_count
    _result['cows'] = _cows_count
    return _result


def complete_the_game():
    return _result['bulls'] == 4



