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

#题 11：match-case HTTP 状态码
def http_status(code):
   match code:
         case 200:
           return 'OK'
         case 404:
            return 'Not Found'
         case 500:
            return 'Internal Server Error'
         case _:
            return 'Unknown Status Code'
print(http_status(200))  # 输出: OK
print(http_status(404))  # 输出: Not Found
print(http_status(500))  # 输出: Internal Server Error

#题 12：九九乘法表
"""for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    print()"""

#题 13：while 密码验证
def password_check(correct_p="123456", max_attempts=3):
    for i in range(max_attempts):
        pwd=input(f"第{i+1}次请输入密码：")
        if pwd==correct_p:
            print("密码正确，登录成功！")
            return True
        else:
            print("密码错误，请重试。")
    print("尝试次数过多，登录失败。")
       
#password_check()  # 调用函数进行密码验证

#题 14：for + continue
def for_continue_example(n):
    for i in range(1,int(n)+1):
        if i % 3 == 0:
            continue  # 跳过偶数
        print(i, end=" ")  # 输出奇数

for_continue_example(10)  # 输出: 1 2 4 5 7 8

#题15 闭包 make_adder
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_5 = make_adder(5)
print(add_5(10))  # 输出: 15
print(add_5(20))  # 输出: 25
print(type(add_5))  # 输出: <class 'function'>

#题 16：默认参数陷阱
def func(a=None):
    a = []
    a.append(1)
    return a
print(func())
print(func())

#题 17：**kwargs 过滤
def filter_kwargs(**kwargs):
    return{k:v for k,v in kwargs.items() if isinstance(v,(int,float)) and not isinstance(v,bool)}

print(filter_kwargs(a=1, b='hello', c=3.5, d=[1, 2]))  # 输出: {'a': 1, 'c': 3.5}
print(filter_kwargs(a=1, b="x", c=3.14, d=True))  # {'a': 1, 'c': 3.14}

#题 18：lambda 排序
lst = [('a', 3), ('b', 1), ('c', 2)]
sorted_lst=sorted(lst,key=lambda x:x[1],reverse=True)
print(sorted_lst)  # 输出: [('a', 3), ('c', 2

#题 19：LEGB 与作用域

#题 20：计时装饰器
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"函数 {func.__name__} 执行时间: {end-start:.6f} 秒")
        return result
    return wrapper

@timer
def example_function():
    time.sleep(0.1)  # 模拟耗时操作
    return "函数执行完成"

print(example_function())  # 输出: 函数 example_function 执行时间: 0.100xxx 秒

#题 25：上下文管理器 Timer
import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end =time.time()
        print(f"耗时 {self.end-self.start:.4f}s")

with Timer():
    time.sleep(0.5)

#题 26：继承与多态
class   Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

animals=[Dog(),Cat()]
for a in animals:
    print(a.speak())

#七、文件与异常（3 题）
from pathlib import Path

def line_lengths(p):
    try:
        with Path(p).open(encoding='utf-8') as f:
            return [len(line) for line in f]
    except FileNotFoundError:
        return []

print(line_lengths('README.md'))

#题 28：自定义异常
import math

class NegativeNumberError(Exception):
    pass

def sqrt_safe(n):
    if n <0:
        raise NegativeNumberError("不能对负数开平方")
    return math.sqrt(n)

try:
    print(sqrt_safe(-1))
except NegativeNumberError as e:
    print(e)

#题 29：批量重命名文件（模拟）
from pathlib import Path

def plan_rename():
    md_files=list(Path('.').glob('*.md'))
    for i,f in enumerate(md_files,1):
        new_name=f"file_{i:03d}.txt"
        print(f"{f.name}->{new_name}") 

plan_rename()