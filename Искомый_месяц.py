month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
month_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# объявление функции
def get_month(language, number):
    if language == 'ru':
      return month_ru[number-1]
    else:
      return month_en[number-1]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))