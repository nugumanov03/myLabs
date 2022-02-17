sum = 0
k = input()
for char in k:
    sum+=ord(char)

if sum > 300:
    print("It is tasty!")
else: print("Oh, no!")
