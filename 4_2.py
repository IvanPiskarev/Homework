import json
data = {"test": "123"}
with open("data.json", "w") as f:
	json.dump(data, f)
login = input("Введите логин")
password = input("Введите пароль")
def register(login, password):
	if login not in data.keys():
		data[login] = password
		with open("register.json", "w") as f:
			json.dump(data, f)
		print("Вы успешно зарегистрированы")
	else:
		print("Логин занят")
register(login, password)