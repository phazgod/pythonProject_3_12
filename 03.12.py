def fill_set():
    _set = dict()
    s = input()
    while s != '':
        _s = s.split()
        _set[_s[0] + _s[1]] = int(_s[2])
        s = input()
    return _set


_i = dict()
_m = dict()
_p = dict()


count = int(input())
_list_dict = [0] * count
for i in range(count):
    _list_dict[i] = fill_set()

for _set in _list_dict:
    print(_set)