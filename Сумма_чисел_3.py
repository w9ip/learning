lst = [int(e) for e in input().split()]
sum_res = sum(lst)
print('+'.join([str(e) for e in lst]) + '=' + str(sum_res))
