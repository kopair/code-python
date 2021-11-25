two_thing = "one two three"

arr = two_thing.split(" ")

more_stuff = ["one","two","three","four","five","six","seven","eight","nine","ten"]

while len(arr) != 10:
  next_one = more_stuff.pop()
  print("next_one",next_one)
  arr.append(next_one)
  print(f"now the length {len(arr)}")

print("now:",arr)

print(arr[1])
print(arr[-1])
print(arr.pop())
print(" ".join(arr))
print("#".join(arr[3:5]))

print(arr.index("one"))