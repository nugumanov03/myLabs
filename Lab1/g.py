s = input()
sum = 0
i=0
while i != len(s):
    if s[i] =='1':
        sum+=pow(2,len(s)-1-i) 
    i+=1

print(sum)