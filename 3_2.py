s = "fnenfen fejfejfjefjefj fejjf fej feu9fw9ef fje euu eifi ee fejfje"
d = list(s.split())
def words(d):
	x = [i for i in d if len(i) < 5]
	return x
print(words(d))