l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
h = {i for i in l if l.count(i) > 1}
print(h)
