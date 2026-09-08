def test_demo_output():
    name = "Alice"
    age = 30
    height = 1.75
    message = f"My name is {name}, my age is {age}, my height is {height} meters."
    
    assert message in "My name is Alice, my age is 30, my height is 1.75 meters."

def test_string_methods():
    s = "hello"        
    assert s.upper() == "HELLO"
    assert s.lower() == "hello"
    assert len(s) == 5

# tests/test_file_type.py
from utils.lists import file_type  # 替换为实际模块名

def test_known():
    assert file_type('a.xlsx') == 'Excel file'

def test_unknown():
    assert file_type('a.xyz') == 'Unknown file type'

def test_case():
    assert file_type('A.XLSX') == 'Excel file'
