print("." * 10)
print("a" + "d" + "s" + "e" + "p", end="     ")

formatter = "{}{}{}{}"
print(formatter.format("hs","as","ds","dd"))
print(formatter.format(1,2,3,9))
print(formatter.format(formatter,formatter,formatter,formatter))