# 类
class People(object):
  def __init__(self,name,age):
      self.name = name
      self.age = age
      self.jump()
  def walk(self):
    print("{} 在走路".format(self.name))
  def eat(self):
    print("{}在吃饭".format(self.name))
  def jump(self):
    print("{}跳了一下".format(self.name))

xiaoer = People("小儿",12)
wangwu = People("王五",123)
