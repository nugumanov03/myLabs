
amount = int(input())
li = []
i = 0
while i !=amount:
    li.append(int(input()))
    i+=1


i = 0
while i !=amount:
    element = li[i]
    if element <= 10:
        element = 'Go to work!'
    elif element > 10 and element <= 25:
        element = 'You are weak'
    elif element  > 25 and element <= 45:
        element = 'Okay, fine'
    elif element > 45:
        element = 'Burn! Burn! Burn Young!'
    li[i] = element 
    i+=1

i = 0
while i !=amount:
    print(li[i])
    i+=1
