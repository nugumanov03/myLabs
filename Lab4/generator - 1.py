def squares(n):
    for i in range(n):
        yield i**2
        
a = squares(15)
for i in a:
    print(i)
 