li = list(map(int, input().split()))
leng = li[0]
try:
    x = li[1]
except:
    x=int(input())
li1 = []
xor = 0
for i in range(leng):
    i= x +2*i
    li1.append(i)
for i in range(leng):
    xor = xor ^ li1[i]

print(xor)