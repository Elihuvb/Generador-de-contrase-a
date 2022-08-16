import random


def password_generator():
    mayusculas = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    minusculas = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    signos = [
        "!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¡", "¿", "@", "{",
        "}"
    ]

    caracteres = mayusculas + minusculas + numeros + signos

    password_gen = []

    for i in range(15):
        caracteres_random = random.choice(caracteres)
        password_gen.append(caracteres_random)

    password_gen = ''.join(password_gen)
    return password_gen


def run():
    password = password_generator()
    print("Tu nueva contraseña es " + password)


if __name__ == '__main__':
    run()
