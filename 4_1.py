import json
login = input("Введите логин")
password = input("Введите пароль")
def register(login, password):
	data = {}
	data[login] = password
	with open("register.json", "w") as f:
		json.dump(data, f)
register(login, password)