# Password Security Checker
# Projet cybersécurité - niveau débutant

import re

password = input("Entre un mot de passe : ")

score = 0

# Longueur
if len(password) >= 8:
    score += 1

# Majuscule
if re.search(r"[A-Z]", password):
    score += 1

# Minuscule
if re.search(r"[a-z]", password):
    score += 1

# Chiffre
if re.search(r"[0-9]", password):
    score += 1

# Caractère spécial
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nRésultat :")

if score <= 2:
    print("Mot de passe FAIBLE ❌")
elif score == 3 or score == 4:
    print("Mot de passe MOYEN ⚠️")
else:
    print("Mot de passe FORT ✅")

