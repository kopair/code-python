# -*- coding: utf-8 -*-
fobj = open('String.txt')
contain = fobj.read()
char = ''
for i in contain:
    if i.isdigit():
        char += i
print(char)
fobj.close()