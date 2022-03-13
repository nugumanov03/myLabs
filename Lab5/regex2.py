import re
text = input()
tx = re.findall(r"ab{2,3}", text)
print(tx)