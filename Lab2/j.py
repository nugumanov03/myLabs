
n = int(input())

def pas(string):
    if low(string) and up(string) and dig(string):
        return True

def low(string):
    for i in string:
        if i.islower():
            return True         
def dig(string):
    for i in string:
        if i.isdigit(): 
            return True 
def up(string):
    for i in string:
        if i.isupper(): 
            return True 
                               

    
li = []
cnt = 0
for i in range(n):
    string = input()
    if pas(string):
        li.append(string)
li1 = []
for i in li:
    if i not in li1:
        li1.append(i)
        cnt+=1

print(cnt)
li1.sort()
for i in li1:
    print(i)