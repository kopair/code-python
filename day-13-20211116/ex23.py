# 一个问答游戏
print('''you enter a dark room with two doors.
Do you go through door #1 or door #2? ''')

door = input('<')

if door == "1":
  print("There's a gaint bear here eating a cheese cake.")
  print("What do you do?")
  print("1.Take the cake.")
  print("2. Scream at the bear.")

  bear = input("<")

  if bear == "1":
    print("the bear eats your face off,Good job!")
  elif bear == "2":
    print("the bear eats your legs off,Good job!")
  else:
    print(f"doing {bear} is probably better")
    print(" Bear runs away")
elif door == "2":
  print("You stare into the endless abyss at ")
  print("1.Blueberries.")
  print("2.Yellow jacket")
  print("3.Understanding")
  insanity = input("<")
  if insanity == "1" or insanity == "2":
    print("Good job")
  else:
    print("So sad!")
else:
  print("you stumble around and fall on a knife and die ,Good job!")
