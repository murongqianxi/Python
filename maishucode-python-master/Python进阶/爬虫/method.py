# from collections import Counter

# s = "asdghpqgngnergheqr;'kjageqr"
# res = Counter(s)
# print(res)

a = [1,2,3,4,5]

def func(n):
    return n * n

res = map(func, a)
#res = [i for i in res]
print(list(res))

from functools import reduce

a = reduce(lambda x, y: x + y, range(1, 101))
print(a)

print(sum(range(1,101)))