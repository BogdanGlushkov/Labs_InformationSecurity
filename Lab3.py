import random
import sympy


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keypair(bits=12):
    p = sympy.randprime(2 ** bits, 2 ** (bits + 1))
    g = sympy.randprime(2, p - 1)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    public_key = (p, g, h)
    private_key = x
    return public_key, private_key


def encrypt(message, public_key):
    p, g, h = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(h, k, p)
    c2 = [(s * ord(char)) % p for char in message]
    return c1, c2


def decrypt(c1, c2, private_key, public_key):
    p, _, _ = public_key
    s_inv = mod_inverse(pow(c1, private_key, p), p)
    decrypted_message = ''.join([chr((s_inv * c) % p) for c in c2])
    return decrypted_message


def main():
    message = "Hey there! How are you? Hope everything's great on your end. The weather here is just magical today. Any exciting plans for the weekend? If you need company or advice, I'm always happy to help. Drop me a message if you'd like! Drop me a message if you'd like! Drop me a message if you'd like!"
    len(message)

    if len(message) < 256:
        print("Ошибка: Длина сообщения должна быть не менее 256 символов.")
        return

    public_key, private_key = generate_keypair(bits=12)
    print("Открытый ключ:", public_key)

    c1, c2 = encrypt(message, public_key)
    print("Зашифрованные данные:")
    print("C1:", c1)
    print("C2:", c2)

    decrypted_message = decrypt(c1, c2, private_key, public_key)
    print("Расшифрованное сообщение:", decrypted_message)


if __name__ == "__main__":
    main()
