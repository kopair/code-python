# 学习else 和 elif
people = 30
dogs = 10
cats = 50

if people <= dogs:
  print("less people")
elif people <= cats:
  print("more cats")
else:
  print("ahahah")

# 加上or和and的一些练习

if people <= dogs and people <= cats:
  print("less")
elif people >= dogs and people >= cats:
  print("more")
else:
  print("haha")

if people <= dogs or people <= cats:
  print("less")
elif people >= dogs or people >= cats:
  print("more")
else:
  print("haha")