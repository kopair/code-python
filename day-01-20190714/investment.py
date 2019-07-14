# -*- coding: utf-8 -*-
amount = float(input('Enter a amount:'))
inrate = float(input('Enter a inrate:'))
period = int(input('Enter a period:'))
value = 0
year = 1
while year <=period:
    value = amount + (amount * inrate)
    print('every year {} rate {:.2f}'.format(year,value))
    amount = value
    year += 1