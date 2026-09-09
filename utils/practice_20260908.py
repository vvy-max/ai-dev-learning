#题 21：缓存装饰器
def cache_decorator(func):
    cache={}
    def wrapper(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrapper

@cache_decorator
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(10))  # 输出: 55

#题 22：带参数的重试装饰器（间隔）
import time
def retry_decorator(max_retries,delay):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(max_retries):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"attempt{i+1}failed:{e}")
                    if i==max_retries-1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry_decorator(max_retries=3,delay=0.5)
def might_fail():
    raise ValueError("Random failure")

#might_fail()

#题 题 23：dataclass Point
from dataclasses import dataclass
import math

@dataclass
class Point:
    x:float
    y:float
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

p1=Point(0,0)
p2=Point(3,4)
print(p1.distance(p2))