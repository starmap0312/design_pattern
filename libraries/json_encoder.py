import json
from io import StringIO

a_dict = {"key": "value", 5: "five"}
print("json.dumps: convert a python dict to a string")
a_str = json.dumps(a_dict)
print(a_str)

print("json.dumps: convert a python dict to a string with indent=2")
a_str = json.dumps(a_dict, indent=2)
print(a_str)

print("json.loads: convert a string to a python dict")
a_dict = json.loads(a_str)
print(a_dict)

print("json.dump: dump a python dict to a file")
io = StringIO()
json.dump(a_dict, io)
print(io.getvalue())

print("json.load: load a file to a python dict")
io = StringIO(io.getvalue())
print(json.load(io))
