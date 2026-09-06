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
print(message)
print(message.format(**table))

for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    print(repr(x*x*x).rjust(4))
