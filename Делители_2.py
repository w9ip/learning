def get_factors(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst


def number_of_factors(num):
    return len(get_factors(num))


print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
