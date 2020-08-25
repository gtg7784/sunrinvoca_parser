a = [
  {'day': 1},
  {'day': 2}
]

b = [1 == i['day'] for i in a]

print(b)