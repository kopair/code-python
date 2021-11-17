# 学习if语句
people = 50
cats = 30
dogs = 10

if people < cats:
  print("less people")

if people <= dogs:
  print("more dogs")

if people > cats:
  print("more people")

if people >= dogs:
  print("less dogs")

dogs += 40
if people == dogs:
  print("equal")