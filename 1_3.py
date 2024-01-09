x = int(input("Введите число"))
s = 0 
while x > 0:
    t = x % 10
    s = s + t
    x = x // 10
print(s)