import json

a=33
b=42

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": a},
    {"model": "Ford Edge", "mpg": b}
  ]
}

print(json.dumps(x))