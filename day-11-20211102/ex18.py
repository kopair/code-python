# ex24.py 练习
print("lianxi")
print(' you\'d need know \'d with \\ that do:')
print('adas \t ss')

poem = """
\t ads as 
\n sdffff
\n\t asdddddd
"""
print(poem)
print('============')

five = 10+20/4-5
print(f"this num :{five}")

def de_start(started):
  jelly = started * 200
  jars = started / 100
  created = started / 1000
  return jelly,jars,created

started_point = 100000
one,two,three = de_start(started_point)

print("asdsd{}".format(started_point))
print(f"one,two,trhee,{one},{two},{three}")

# 新的输出方式
started_num = 90000
allnum = de_start(started_num)
print("one,{};two,{};three,{}".format(*allnum))
