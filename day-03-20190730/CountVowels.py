# -*- coding: utf-8 -*-
import collections
from collections import Counter

num = input('Enter a String:')
common = Counter(num).most_common()
for i in 'aeuoi':
    for (item,index) in common:
        if i==item:
            print('{}: {}'.format(item,str(index)))
