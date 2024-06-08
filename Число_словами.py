len_1 = [
      'один',
      'два',
      'три',
      'четыре',
      'пять',
      'шесть',
      'семь',
      'восемь',
      'девять',
      ]
len_2 = [
      'десять',
      'двадцать',
      'тридцать',
      'сорок',
      'пятьдесят',
      'шестьдесят',
      'семьдесят',
      'восемьдесят',
      'девяносто',
      ]
len_2_ = [
        'одиннадцать',
        'двенадцать',
        'тринадцать',
        'четырнадцать',
        'пятнадцать',
        'шестнадцать',
        'семнадцать',
        'восемнадцать',
        'девятнадцать'
        ]
def return_len(num):
  if 0 <= num <= 9:
    return 1
  else:
    return 2

def return_len_1(num):
  if num == 0:
    return 'ноль'
  else:
    return len_1[num-1]

def number_to_words(num):
    if return_len(num) == 1:
      return return_len_1(num)
    elif num // 10 == 1:
        if num % 10 == 0:
            return 'десять'
        else:
            return len_2_[num % 10 - 1]
    elif num // 10 > 1:
      if num % 10 == 0:
        return len_2[num // 10 - 1]
      else:
        return len_2[num // 10 - 1] + ' ' + return_len_1(num % 10)
        
  
n = int(input())
print(number_to_words(n))