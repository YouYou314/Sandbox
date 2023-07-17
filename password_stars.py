password = input(“Enter password: ”)

while len(password) < MININUM_LENGTH:
	print(“Invalid input”)
	password = input(“Enter password: ”)

print(len(password) * “*”)

