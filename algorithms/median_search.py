import random

def partition(A, lo, hi, idx):
    """ Разделение А на две части относительно значения А[idx]. """
    if lo == hi: return lo
    
    A[idx], A[lo] = A[lo], A[idx]  # ставим в нужную позицию
    i = lo
    j = hi + 1
    
    while True:
        while True:
            i += 1
            if i == hi: break
            if A[lo] < A[i]: break
        
        while True:
            j -= 1
            if j == lo: break
            if A[j] < A[lo]: break
            
        if i >= j: break
        A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j
def linear_median(A):
    """
    Быстрая реализация поиска медианы в произвольном списке.
    Предполагается, что в списке нечетное число элементов.
    Обратите внимание на то, что при работе алгоритма
    порядок элементов в А меняется.
    """
    lo = 0
    hi = len(A) - 1
    mid = hi // 2
    while lo < hi:
        idx = random.randint(lo, hi)  # Случайный выбор допустимого индекса
        j = partition(A, lo, hi, idx)
        
        if j == mid:
            return A[j]
        if j < mid:
            lo = j + 1
        else:
            hi = j-1
    return A[lo]
A = [2, 3, 1, 6, 4, 5] 
print(linear_median(A))
print(A)