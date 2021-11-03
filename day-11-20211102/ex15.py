from sys import argv
script, file_name = argv

def print_all(f):
  print(f.read())

# seek(0)表示重新定位在文件的第0位及开始位置，可以不用再次打开文件
def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print(line_count,f.readline())

current_file = open(file_name)

print("read all file:\n")
print_all(current_file)

print("let's rewind")
rewind(current_file)

print("read three line:")

current_line = 1
# 执行readline是会记录上次读取位置，所以和传入的current_line无关
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
