import json
from io import StringIO

# 对基本的 Python 对象层次结构进行编码：
a = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(a)
print(type(a))
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

io = StringIO()
json.dump(['streaming api'], io)
io_value = io.getvalue()
print(io_value)
print(type(io_value))
