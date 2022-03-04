from datetime import date, timedelta
tod = date.today()
yes = date.today() - timedelta(1)
tom = date.today() + timedelta(1)
print("Yesterday :",yes)
print("Today :", tod )
print("Tomorrow :", tom)