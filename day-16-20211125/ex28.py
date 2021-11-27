# 字典
states = {
  'asd' : ' ASD',
  'S' : 's',
  'qwewe' : 'QWEWE',
  'wewewe' : 'WEWEWE'
}
cities = {
  "s" : "city",
  "P" : "provice",
  "CO" : "Contry",
  "asd" : "s"
}

cities["C"] = "ccccc"
cities["AA"] = "AAAAA"
print("cities",cities)

print("asdada",cities[states["S"]])

# 利用key来获取value 
print(cities["s"])
print(cities.get('s'))
# 当没有d这个key相关的value值时使用后面这个值
print(cities.get('d','sadas'))
cities['d'] = 'ceshi'
print(cities.get('d','sadas'))

# 集合
example_list = {1,2,3,4,'23','4343'}
list1 = [1,2,3333,4444,2,2,1]
# 有去重功能  列表可以利用set方法转为集合，但是因为集合是无序的，所以将集合利用list转为列表时，可能会导致顺序有问题

print(set(list1))
print(list(set(list1)))