from sqlalchemy import create_engine
import pandas

engine = create_engine('postgresql+psycopg2://w9i@localhost/w9i')

result = pandas.read_sql("""SELECT title, price, 
    (price*18.0/100.0)/(1.0+18.0/100.0) AS tax, 
    price/(1.0+18.0/100.0) AS price_tax 
FROM book""", engine)

"""
В конце года цену всех книг на складе пересчитывают – снижают ее на 30%. 
Написать SQL запрос, который из таблицы book выбирает названия, авторов, количества и вычисляет новые цены книг. 
Столбец с новой ценой назвать new_price, цену округлить до 2-х знаков после запятой.
"""
print(result)
