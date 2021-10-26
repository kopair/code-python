from sys import argv
script, file_name = argv
print(f"We're going to erea {file_name}")
print("If you don't want that, hit control-C")
print("if you want that,hit return")

input('?')

print("opening the file...")
# open代表打开该文件，
# w参数的含义：	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
target = open(file_name,'w')

# 当使用了w参数时，可以不使用截断字符
# 截断字符，截断之后后面全部字符会被删除
print("truncating the file ,bye")
target.truncate()


print("Now I'm going to ask you for three lines")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

# 将输入写入该文件
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 关闭文件
print("finally,I close it")
target.close()

