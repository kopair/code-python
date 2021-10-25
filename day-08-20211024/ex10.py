from sys import argv
script, filename = argv

# 打开文件
txt = open(filename)

print(f"Here's your file {filename}")
# 读取文件
print(txt.read())
# 关闭文件
txt.close()

print("read other file again:")
file_again = input("> ")

text_again = open(file_again)
print(text_again.read())