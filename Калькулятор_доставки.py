def get_shipping_cost(quantity):
    total = 1000
    for i in range(1, quantity):
        total += 120
    return total

print(get_shipping_cost(1))
print(get_shipping_cost(3))