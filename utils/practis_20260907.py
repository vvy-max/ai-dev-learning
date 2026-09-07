#题 1：任意参数求平均值
def average(*args):
    return sum(args)/len(args) if args else 0

print(average(1, 2, 3, 4, 5))  # 输出: 3.0
print(average())  # 输出: 0

#f-string 格式化
from math import pi

print(f"圆周率的值是: |{pi:^10.2f}|")  # 输出: 圆周率的值是: 3.14

#题 3：回文判断
def is_palind(s):
    cleaned="".join(c.lower() for c in s if c.isalnum())
    print(cleaned)
    return cleaned == cleaned[::-1]

print(is_palind("A man, a plan, a canal: Panama"))  # 输出: True
print(is_palind("race a car"))  # 输出: False

#题 4：生成器表达式与类型转换
def g_s(*args):
    lst1=[]
    for i in args:
        lst1.append(int(i))
    sum1=0
    for i in lst1:
        sum1+=i*i
    return sum1

print(g_s(1, '2', '3'))  # 输出: 14
print(g_s(4, '5'))     # 输出: 41

data = [1, '2', 3, '4', 5]
gen=(int(x)**2 for x in data)
print(sum(gen))  # 输出: 55

#题 5：最长公共前缀
def longest_common_p(a,b):
    for item in enumerate(zip(a,b)):
        print(item)
    for i,(x,y) in enumerate(zip(a,b)):
        if x!=y:
            print(i,x,y)
            return a[:i]
    print(i,x,y)
    return a[:i+1]
    #return min(a,b,key=len)

print(longest_common_p("flower", "flow"))  # 输出: "flow"
print(longest_common_p("dog", "racecar"))  # 输出: ""

#题 6：相邻元素求和
def sum_adjacent(lst):
    return [lst[i]+lst[i+1] for i in range(len(lst)-1)]

print(sum_adjacent([1, 2, 3, 4]))  # 输出: [3, 5, 7]

#题 7：斐波那契生成器
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

f=fib()
for i in range(10):
    print(next(f),end=" ")  # 输出: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

#题 8：嵌套元组展平
t = ((1, 2), (3, 4), (5, 6))
flat=[x for sub in t for x in sub]
print(flat)  # 输出: [1, 2, 3, 4, 5, 6]

#题 9：切片反转列表
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))  # 输出: [5, 4, 3, 2, 1]

#题 10：zip 合并字典#
keys = [1, 2, 3]
vals = ['a', 'b', 'c']
d=dict(zip(keys, vals))
for item in zip(keys, vals):
    print(item)
print(d)  # 输出: {1: 'a', 2: 'b', 3: 'c'}