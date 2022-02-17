stroka = ''
st = input()
listslov = st.split()
i = 0;
while i != len(listslov):
    if len(listslov[i]) > 2:
        stroka += listslov[i]
        stroka += ' '
    i+=1

print (stroka)
