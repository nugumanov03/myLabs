leng = int(input())
li = list(map(int, input().split()))
li.sort()
print(int(li[leng-1])*int(li[leng-2]))
