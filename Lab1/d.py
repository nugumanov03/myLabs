

main = int(input())
char = input()

if char == 'k':
    output = main /1024
    presis = int(input()) 

    print(format(output, f'.{presis}f'))
    


elif char == 'b':
    output = main * 1024
    print(output)