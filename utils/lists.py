#练习 1-1：列表推导式生成偶数降序
evens = sorted([x for x in range(1, 21) if x % 2 == 0], reverse=False)
print(evens)

#练习 1-2：递归展平嵌套列表
def flatten(x):
    out=[]
    for i in x:
        if isinstance(i, list):
            out += flatten(i)
        else:
            out.append(i)
    return out

nested = [[1, 2], [3, [4, 5]], 6]
print(flatten(nested))  # 输出: [1, 2, 3, 4, 5, 6]

#练习 1-3：字典按值降序返回键
d={'a': 3, 'b': 1, 'c': 2}
#result = sorted(d,reverse=True)
result = sorted(d, key= lambda k: d[k], reverse=True)
print(result)  # 输出: ['c', 'b', 'a']

#编写代码，给定字典 d={'a':3,'b':1,'c':2}，按键降序返回值的列表。
sorted_values=sorted(d, key=lambda k: d[k], reverse=True)
result_key=[d[k] for k in sorted_values]
print(result_key)  # 输出: [3, 2, 1]
print(d)  # 输出: ['a', 'c', 'b']
print(d.items())  # 输出: dict_items([('a', 3), ('b', 1), ('c', 2)])

#练习 1-4：match-case 文件类型判断
def file_type(filename):
    match filename.rsplit('.',1)[-1].lower():
        case 'xlsx'|'xls':
            return 'Excel file'
        case 'docx'|'doc':
            return 'Word file'
        case 'pptx'|'ppt':
            return 'PowerPoint file'
        case 'pdf':
            return 'PDF file'
        case 'txt':
            return 'Text file'
        case _:
            return 'Unknown file type'

print(file_type('report.xlsx'))  # 输出: Excel file
print(file_type('document.docx'))  # 输出: Word file
print(file_type('presentation.pptx'))  # 输出: PowerPoint file
print('document.pdf'.rsplit('.',1)[-1].lower())  # 输出: PDF file


#练习 1-5：安全除法
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))  # 输出: 5.0
print(safe_divide(10, 0))  # 输出: None

#练习 1-6：Counter 统计
from collections import Counter
lst = ['a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'f', 'a', 'b']
result = Counter(lst).most_common(3)
print(result)  # 输出: Counter({'a': 4, 'b': 3, 'c': 1})

#练习 1-7：重试装饰器（阶段一最难题之一）

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
#print(message)
#print(message.format(**table))

#for x in range(1, 11):
    #print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    #print(repr(x*x*x).rjust(4))

print('20260906')  # 输出: 00012

#练习 1-7：重试装饰器（阶段一最难题之一）
def retry(times):
    def deco(fn):
        def wrap(*a,**k):
            for i in range(times):
                try:
                    print(f"尝试第{i+1}次")
                    return fn(*a,**k)
                except Exception as e:
                    if i== times-1:
                        print(f"第{i+1}次失败，不再重试，抛出异常")
                        raise
                    print(f"第{i+1}次失败，继续重试")
            return None
        return wrap
    return deco

@retry(3)
def might_fail():
    import random
    if random.random() < 0.1:
        raise ValueError("Random failure!")
    return "Success!"
print(might_fail())  # 输出: Success! 或抛出 ValueError

import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrap(*a,**k):
        t0=time.time()
        ret=func(*a,**k)
        print(f"Function {func.__name__} took {time.time()-t0:.4f} seconds")
        return ret
    return wrap

@timer
def slow():
    time.sleep(0.2)
    return "Done!"

slow()  # 输出: Function slow took 2.0000 seconds


def retry_t(times):
    def deco(fn):
        @functools.wraps(fn)
        def wrap(*a,**k):
            for i in range(times):
                try:
                    print(f"尝试第{i+1}次")
                    return fn(*a,**k)
                except Exception as e:
                    if i== times-1:
                        print(f"第{i+1}次失败，不再重试，抛出异常")
                        raise
                    print(f"第{i+1}次失败，继续重试")
            return None
        return wrap
    return deco

@retry_t(3)
def might_fail_t():
    import random
    if random.random()<0.0:
        raise ValueError("Random failure!")
    return "Success!"
print(might_fail_t())  # 输出: Success! 或抛出 ValueError

                   
#练习 1-8：pathlib 安全读文件
import pathlib
def safe_read(f_p):
    try:
        with pathlib.Path(f_p).open('r', encoding='utf-8') as f:
            pathlib.Path(f_p).write_text('Hello, World!', encoding='utf-8')
            return f.read()    
    except FileNotFoundError:
        print(f"文件 {f_p} 未找到")
        return ''

print(safe_read('example.txt'))  # 输出文件内容或提示文件未找到
print(safe_read('nonexistent.txt'))  # 输出: 文件 nonexistent.txt 未找到


#练习 1-9：不可变配置类
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path
import os

# 定位上一级目录的.env
base_dir = Path(__file__).resolve().parent.parent
#env_path = base_dir / ".env"
env_path = base_dir / ".venv"
print(f"当前脚本: {Path(__file__).resolve()}")
print(f"base_dir: {base_dir}")
print(f"env_path: {env_path}")
print(f"文件是否存在: {env_path.exists()}")

load_dotenv(dotenv_path=env_path)

print(env_path.exists())    # True代表文件找到了
print(os.getenv("DB_URL"))  # 看是否读到值
print("DB_URL raw:", os.getenv("DB_URL"))

@dataclass(frozen=True)
class Config:
    db_url: str
    api_key: str

# 从环境变量构造实例，不硬编码密钥
config = Config(
    db_url=os.getenv('DB_URL', ''),
    api_key=os.getenv('API_KEY', '')
)

print(config.db_url)      # .属性名访问
# config.db_url = 'new'   # ❌抛 FrozenInstanceError，frozen=True 实例不可修改

#练习 1-10：pytest 测试 file_type 函数

#题目：写 3 个 pytest 用例测试 1-4 的 file_type 函数（覆盖已知、未知、大小写混合）。

#练习 1-11：pdb 定位 bug
import pdb

def calc():
    pdb.set_trace()  # 设置断点
    data=[1,2,"3"]
    res=sum(data)  # 这里会抛 TypeError，因为 "3" 是字符串
    return res

#calc()  # 调试时会停在断点，检查 data 的类型

#练习 1-12：LEGB 作用域（概念题）
import pdb
def outer():
    #pdb.set_trace()  # 设置断点
    x = []          # Enclosing 作用域
    def inner():
        x.append(1) # 捕获外层可变变量 x
        print(f"inner x: {x}")  # 打印当前 inner 的 x
        return x
    return inner

f = outer()
print(f())  # [1]
print(f())  # [1, 1]  x 被保留

funcs = []
for i in range(3):
    def f():
        print(i)
    funcs.append(f)
    print(f)

funcs[0]() #输出2，不是0
funcs[1]() #输出2，不是1
funcs[2]() #输出2
