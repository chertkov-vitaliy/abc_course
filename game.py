import  random

_dict = {'False': 'Логическое значение', 'None': 'Пустой'}
keys = list(_dict.keys())
ind = random.randint(0, len(keys) - 1)
secret = keys[ind]
mask = [' * '] * len(secret)

def show_describe():
    """ Выводит описание слова  """
    print(_dict[secret])


def show_secret():
    """ Выводит слово """
    for val in mask:
       print(val, end="")


def get_letter():
    letter = input("\n Введите букву:")
    return letter


def check_letter( letter):
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = f" {letter} "


def start():
    while ( " * " in mask):
        show_describe()
        show_secret()
        letter = get_letter()
        check_letter(letter)

start()