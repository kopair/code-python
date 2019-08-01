# -*- coding: utf-8 -*-
import collections
from collections import Counter

num = input('Enter a String:')
common = Counter(num).most_common()
#print(Counter(num).most_common())