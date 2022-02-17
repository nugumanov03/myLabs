# n = int(input())
# f = int(input())

n,f =map(int,input().split())
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

if n <=500 and IsPrime(n) and (f%2 == 0):
    print('Good job!')
else:
    print('Try next time!')
