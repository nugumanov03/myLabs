s = input()
char = input()
st = ''
li = []
i=0
while i != len(s):
    if s[i] == char:
        # print(i)
        li.append(int(i))
        st+= str(i)
    i+=1



print(li[0],end=' ') 
if li[0] != li[len(li)-1]:
    print(li[len(li)-1])

