# 将一个文件复制到另一个文件
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# 只读这个内容，不改变任何
in_file = open(from_file)
indate = in_file.read()

# len函数返回该文件的长度
print(f"The input file is {len(indate)} bytes long")
# 判断文件是否存在
print(f"Does the file exists? {exists(to_file)}")
print("control-C to abor,return to continue")

input()


out_file = open(to_file,'w')
# 写入这个文件内容
out_file.write(indate)

print("Alright,all done ")

out_file.close()
in_file.close()