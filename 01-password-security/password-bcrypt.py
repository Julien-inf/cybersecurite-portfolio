import bcrypt

password = input("Mot de passe : ").encode()

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Hash bcrypt :", hashed)

