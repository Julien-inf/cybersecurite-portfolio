import re
import hashlib  # Module pour le hash

password = input("Entre un mot de passe : ")

score = 0

# Vérifications de sécurité
if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"[0-9]", password):
    score += 1
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nRésultat :")

if score <= 2:
    print("Mot de passe FAIBLE ❌")
elif score <= 4:
    print("Mot de passe MOYEN ⚠️")
else:
    print("Mot de passe FORT ✅")

# HASH du mot de passe (SHA-256)
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nHash SHA-256 du mot de passe :")
print(hashed_password)

