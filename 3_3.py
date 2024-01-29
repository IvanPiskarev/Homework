j = [56, 9, 11, 2]
print(j)
j.sort(key = lambda x: int(str(x)[0]), reverse=True)
print(str(j).replace(", ", ""))