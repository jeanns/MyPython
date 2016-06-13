#!/usr/bin/env python
# -*- coding: utf-8 -*-

###Example 2.1 格式化打印一个字典中的各项元组
'''
def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.
    Return string."""
    return ";".join(["%s=%s" %(k, v) for k,v in params.items()])  #连接字典中的元组对，并以“；”分开,注意此种用法

if __name__ == "__main__":
    myParams = {"Server": "mpilgrim", \
                "database": "master", \
                "uid": "sa", \
                "pwd": "secret" \
                }


    print buildConnectionString.__doc__     #注意不是通过函数的调用
    print __name__          # 直接运行时，__name__的值为一个特别的缺省值，__main__
    print buildConnectionString.__name__    # 得到的值通常为模块的文件名
    print buildConnectionString(myParams)
    print myParams.items()
'''

### 库的搜索路径
'''
import sys
print sys.path  #指定当前搜索路径的目录列表
print u"=============分割线============"
print sys
sys.path.append('C:\\my\\new\\path')  #向sys.path追加目录名
#print sys.path
'''

###dictionary
'''
d = {"Server": "mpilgrim", "database": "master", "admin":"wangyj"}
print d
print u"=============分割线============"
print d['Server']
print u"=============分割线============"
#print d['server']      #错误，不能打印该项，对大小写敏感
print u"=============分割线============"
d['Server'] = 'pubs'    #更改键值
d['Admin'] = 'admin'    #增加键值
print d
print u"=============分割线============"
d['retrycount'] = 3     #可以是混合类型
print d
print u"=============分割线============"
d[42] = "douglas"       #键值可以是字符，也可以是整型
print d
print u"=============分割线============"
del d[42]               #删除元素
print d
print u"=============分割线============"
d.clear()               #清除所有元素
print d
print u"=============分割线============"
'''

###List
'''
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print li
print li[0]
print li[4]
print li[-1]
print li[-2]
print li[1:3]
print li[0:3]
print li[:3]
print li[3:]
print id(li)
print li[:]     #li[:]是li的拷贝？可实际上好像是别名，两者指向同一对象
print id(li)
li[:]
li.insert(1,1)
print li
print id(li)
li.append("new")
print li
li.remove(1)    #remove:删除第一个出现的值
print li
'''
###list解析
'''
li = [1, 9, 8, 4]
print [elem * 2 for elem in li] #遍历元素并计算
print li  # 对list的解析不改变原始的list
li = [elem * 2 for elem in li] #将解析结果赋值给原始对象是安全、可行的
print li
'''

###tuple
'''
t = ("a", "b", 'mpilgrim', 'z', 'example')
print t
print t[0]
print t[-1]
print t[1:3]
li = list(t)    #将tuple转换为list
print li
t1 = tuple(li)  #将list转换为tuple
'''

### 一次赋多值
'''
v = ('a', 'b', 'c')
(x, y, z) = v
print x, y, z

(a,b,c) = (1,2,3)
print a,b,c
'''
### 连续值赋值
'''
(Monday, Tuesday, Wednesday, Thuesday, Friday, Saturday, Sunday) = range(7) #相当于C里面的enum类型赋值
print Monday, Tuesday, Wednesday
'''

##自省
####Example4.1 aplhelper.py

def info(object, spacing = 10, collapse = 1):
    """Print methods and doc strings.
    Take modules, class, list, dictionary, or string."""

    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)  ## 不明白其意义, " ".join(s.split()) 将字符串转为列表，然后再转为字符串？为何多此一举？  正解：只是为了展示and。。or的技巧
    '''
    print u"\n***可调用的方法列表:*** \n", methodList   #可调用的方法列表
    print u"\n***可调用的方法地址***\n"
    print [getattr(object, method) for method in methodList]    #可调用的方法地址
    print u"\n***可调用的方法说明（列表）***"
    print [getattr(object, method).__doc__ for method in methodList]
    print u"\n***string化的可调用方法说明（列表）***\n"
    print [str(getattr(object, method).__doc__ )for method in methodList]
    print u"\n***将列表中的str子项转化为列表***\n"
    print [str(getattr(object, method).__doc__ ).split() for method in methodList]
    print u"\n***使用join将列表子项转化为字符串"
    print [" ".join(str(getattr(object, method).__doc__ ).split()) for method in methodList]
    print u"\n***连接方法名以及文档介绍内容"
    #print "\n".join(["%s\t %s" % (method.ljust(20), " ".join(str(getattr(object, method).__doc__ ).split())) for method in methodList])
    print "\n".join(["%s %s" % (method.ljust(20), str(getattr(object, method).__doc__ )) for method in methodList])

    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)  ## 不明白其意义, " ".join(s.split()) 将字符串转为列表，然后再转为字符串？为何多此一举？

#    print "\n***info(object):*** \n"

    print "\n".join(["%s%s" %
                     (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
if __name__ == "__main__":
    print u"***info.__doc__内容:"
    print info.__doc__

    li = []
    info(li)
'''


### callable(object)用法 callable(object)用于检查对象object是否可被调用
'''
print callable(0)   #False
print callable("hello") #False

def add(a, b):
    return a + b
print callable(add)     # True
print callable(add(1, 2))   #False

print dir()     # dir()的用法，显示当前范围或指定参数的属性、方法等内容列表

class A:
    def method(self):
        return 0
a = A()
print callable(A)       #True
print callable(a)       #False

class B:
    def __call__(self):
        return 0
b = B()
print callable(B)   #True
print callable(b)   #True，因为类实现了__call__方法，所以其实例b可调用
'''

###getattr(), setattr(), delattr(), hasattr()用法
#getattr()用于返回一个对象属性，或者方法
#setattr(实例对象，属性名，任意值)		// 设置对象的属性值
#delattr(实例对象， 属性名)	// 删除实例中的指定属性
#hasattr(object, name)		//确定一个对象是否具有某个属性

'''
class A:
    def __init__(self):
        self.name = 'jeanns'
        #self.age = 18
    def method(self):
        print "method print"

Instance = A()
print getattr(Instance, 'name', 'not find')     # 如果Instance对象中有属性name，则打印self.name的值，否则打印’not find'
print getattr(Instance, 'age', 'not find')
print getattr(Instance, 'method', 'default')    # 如果Instance对象中有方法method，则打印self.name的值，否则打印’not find'
print getattr(Instance, 'method', 'default')()  # 如果有方法method，运行函数并打印None否则打印default

setattr(Instance, 'sex', 'man')       # 增加sex属性并设置Instance.sex = ‘man'
print Instance.sex

#delattr(Instance, 'sex')
#print Instance.sex
#delattr(Instance, 'name')       # 删除实例中的name属性
#print Instance.name
print dir(Instance)     #dir()方法返回参数的属性、方法列表
print dir(A)

print "++++++++++++"
print hasattr(A, 'method')
print hasattr(Instance, 'name')
print hasattr(Instance, 'sex')
print hasattr(A, 'name')    ## False,类不具有属性，对象才有

print "=================="
li = ["wangyj", "jeanns"]
print getattr(li, 'pop')
print li
getattr(li, 'pop')()    ## 运行li.pop()
print li
getattr(li, 'append')('Moe')  ## 增加一个’Moe'元素
print li
'''

# ljust(width[,fillchar])	//返回一个原字符串左对齐，并使用空格填充至指定长度的新字符串
'''
str = "this is string example...Wow!!!"
print str.ljust(50, 'a')
'''

###lambda()用法
'''
g = lambda x : x ** 2
print g         ##lambda语句构建的其实是一个函数对象

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]         ## filter，map, reduce的用法
print filter(lambda x : x % 3 == 0, foo)    ## 等同于  print [x for x in foo if x % 3 == 0]
print map(lambda x: x * 2 + 10, foo)        ## 等同于  print [x * 2 + 10 for x in foo]
print reduce(lambda x, y : x + y, foo)      ## 等同于  foo[0] + foo[1] + ... + foo[n]
def S():
    sum = 0
    for i in foo:
        sum += i
    return sum
s = S()
print s
'''
###为什么要对一个doc string使用str？
'''
def foo():
    print 2
foo()
print foo.__doc__        // 非字符串“None”
print foo.__doc__        //== None
print str(foo.__doc__)   // 字符串“None”
print type(foo.__doc__)
print type(str(foo.__doc__))
'''


