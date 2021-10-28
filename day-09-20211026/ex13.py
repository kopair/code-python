# def 
# *参数将所有参数都汇合到argv里面，可以再次解构内容
def print_two(*argv):
  argv1,argv2 = argv
  print(f"this is {argv1} and {argv2}")

def print_two_again(argv1, argv2):
  print(f"this is {argv1} and {argv2}")

def print_one(one):
  print(f"this is {one}")

def print_none():
  print("this is nothing")

print_two("asd","sdsd")
print_two_again("we","together")
print_one('only')
print_none()
