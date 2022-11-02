# 2. Палиндром строки

def palindrom(string):
    """
    Палиндром строки
    """

    string = string.replace(" ", '')

    # вернуть полученый результат
    return string == string[::-1]

print(palindrom('taco cat'), palindrom('rotator'), palindrom('black cat'), sep='\n')


# 3. Перевод арабского числа в римское

def convert(num: int) -> str:
    """
    Перевод арабского числа в римское
    """

    # арабские цифры
    arab_num = [0, 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000];

    # римские цифры
    roman_num = ['', 'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'];

    result = ""

    pos = len(arab_num) - 1

    while num > 0:
        if num >= arab_num[pos]:
            result += roman_num[pos]
            num -= arab_num[pos]
        else:
            pos -= 1

    # вернуть результат
    return result


# проверка
print(convert(3), convert(9), convert(1945), sep='\n')


# 4. Валидность скобок

def is_valid(string: str) -> bool:
    """
    Валидность скобок
    """

    brackets = ['()', '{}', '[]']

    while any(x in string for x in brackets):
        for br in brackets:
            string = string.replace(br, '')

    # вернуть полученый результат
    return not string


# проверка
print(is_valid("[{}({})]"), is_valid("{]"), is_valid("{"), sep='\n')


# 5. Умножить два бинарных числа в формате строк

def mult(number1, number2):
    """
    Умножить два бинарных числа в формате строк
    """

    # вернуть результат
    return bin(int(number1, 2) * int(number2, 2))[2:]

# проверка
# введите первое число в 2ой системе:
number1 = '111'

# введите второе число в 2ой системе:
number2 = '101'

# результат
print(mult(number1, number2))