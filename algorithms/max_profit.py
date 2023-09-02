# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Потому что, мы купили акцию в 1-й день (начиная с нулевого).
# Продали в 4-й день за 6.
# 6-1=5

########################################
# цена акции: | 7 | 1 | 5 | 3 | 6 | 4 |#
# дни:        | 0 | 1 | 2 | 3 | 4 | 5 |#
########################################

# Каждый i-ый элемент списка, это акция.
# Каждый i (индекс) это день.
# Необходимо выбрать максимальную прибыль.
# Если прибыль заработать нельзя, то возвращаем 0.


def max_profit(prices):
    if not prices: return 0
    bought_day = prices.index(min(prices))
    sold_day = prices.index(max(prices))
    
    while bought_day > sold_day:
        prices[sold_day] = 0
        sold_day = prices.index(max(prices))
        
    print(prices[sold_day] - prices[bought_day])
    
max_profit([7,1,5,3,6,4]) # 5
max_profit([7,6,4,3,1]) # 0
max_profit([]) # 0
max_profit([2]) # 
max_profit([2, 6, 7, 8, 9, 10])
max_profit([2, 3, 5, 6, 7])
max_profit([2, 1])
max_profit([2, 1, 24, 5, 32, 0, 67])
max_profit([2, 1, 24, 5, 32, 1, 67])
max_profit([2,4,1])
        