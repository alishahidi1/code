from collections import deque
def calbinary(n):
    if n<=0:
        return None
    quo = n//2
    rem = n%2
    while quo != 0:
        return f'{calbinary(quo)}{rem}'
    return f'{rem}'

# for i in range (1,10):
#     print(calbinary(i))

def genbins(n):
    binums = deque()
    for i in range(1,n+1):
        binums.append(calbinary(i))
    return binums

print(genbins(20))