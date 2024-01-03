favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
                    'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
                    'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
                    'anna': 55, 'madlen': 876}

result = {k: favorite_numbers[k] for k in favorite_numbers if
          favorite_numbers[k] % 100 == favorite_numbers[k] and not favorite_numbers[k] % 10 == favorite_numbers[k]}
print(result)
