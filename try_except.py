import os

os.system('COLOR B')


def add_everything_up(a, b):
    try:
        if str(a).isnumeric() and str(b).isnumeric():
            if isinstance(a, float) or isinstance(b, float):
                return round(a + b, 3)
            else:
                return a + b
        else:
            return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

try:
    os.system('PAUSE')
except:
    os.system('CLS')
