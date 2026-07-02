import random
import string

def generar_password():
    longitud = random.randint(8, 14)
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

passwords = set()

while len(passwords) < 1000:
    passwords.add(generar_password())

with open("passwords.txt", "w") as f:
    for pwd in sorted(passwords):
        f.write(pwd + "\n")

print("Se generó passwords.txt con", len(passwords), "contraseñas.")