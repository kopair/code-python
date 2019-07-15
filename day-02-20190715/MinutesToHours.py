# -*- coding: utf-8 -*-
import sys

def Hours(time):
    if time < 0:
        raise ValueError("error")
    else:
        print("{} H, {} M".format(int(time/60),time%60))
try:
    Hours(int(sys.argv[1]))
except:
    print('something wrong')