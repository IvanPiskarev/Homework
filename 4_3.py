import json
data = {"test": "123"}
with open("data.json", "w") as f:
	json.dump(data, f)
login = input("Введите логин")
password = input("Введите пароль")
def login_function(login, password):
	if login in data.keys() and password in data.values():
			print("Успешный вход в систему")
	else:
		print("Неправильный логин или пароль")
login_function(login, password)