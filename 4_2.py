import json
login = input("Введите логин")
password = input("Введите пароль")
def register(login, password):
	with open("data.json", "r") as f:
		data = json.load(f)
	if login not in data.keys():
		data[login] = password
		with open("data.json", "w") as f:
			json.dump(data, f)
		print("Вы успешно зарегистрированы")
	else:
		print("Логин занят")
register(login, password)