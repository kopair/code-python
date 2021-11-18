# for循环
# list数据
the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricots']
change = [1,'one',2,'two',3,'three']

for num in the_count:
  print(f"this num : {num}")

for fu in fruits:
  print(f"this fu : {fu}")

for changes in change:
  print(f"changes: {changes}")
elements = []
for i in range(0,6):
  print(f" this i {i}")
  elements.append(i)
for i in elements:
  print(f"elements i : {i}")

rangeArr = []
rangeArr.append(range(1,10))
print(rangeArr)

for i in rangeArr:
  print(f"elements i : {i}")
