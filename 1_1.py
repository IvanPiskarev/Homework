x = float(input("Введите вклад"))
p = float(input("Введите количество процентов"))
y = float(input("Введите нужную сумму"))
time = 0
while x < y:
	time = time + 1
	x = int(x * (100 + p) / 100)
print(time)