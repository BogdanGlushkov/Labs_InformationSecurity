import random
import math

def is_prime(num):
    """
    Проверяет, является ли число простым.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(bits=16):
    """
    Генерирует простое число с заданным количеством бит.
    """
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида для нахождения наибольшего общего делителя (НОД).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    """
    Находит модульное обратное a по модулю m с использованием расширенного алгоритма Евклида.
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('The modular inverse does not exist')
    else:
        return x % m

def generate_key_pair(bits=16):
    """
    Генерирует открытый и закрытый ключи для алгоритма RSA.
    """
    # Генерация простых чисел p и q
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытой экспоненты e
    e = 65537  # Обычно выбирается 65537, так как это простое число и обеспечивает хорошую производительность

    # Вычисление секретной экспоненты d
    d = modinv(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    """
    Шифрует сообщение с использованием открытого ключа RSA.
    """
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """
    Расшифровывает зашифрованное сообщение с использованием закрытого ключа RSA.
    """
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

def encrypt_file(input_file, output_file, public_key):
    """
    Шифрует текстовый файл с использованием открытого ключа RSA.
    """
    with open(input_file, 'r') as file:
        plaintext = file.read()
    encrypted_message = encrypt(plaintext, public_key)
    with open(output_file, 'w') as file:
        file.write(','.join(map(str, encrypted_message)))

def main():
    # Генерация ключей
    public_key, private_key = generate_key_pair(bits=16)

    # Шифрование
    message = 'Hello, RSA encryption!'
    encrypted_message = encrypt(message, public_key)
    print(f'Зашифрованное сообщение: {encrypted_message}')

    # Расшифрование
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f'Расшифрованное сообщение: {decrypted_message}')

    # Шифрование текстового файла
    input_file = 'input.txt'
    output_file = 'encrypted_file.txt'
    encrypt_file(input_file, output_file, public_key)
    print(f'Файл {input_file} успешно зашифрован и сохранен в {output_file}')

if __name__ == '__main__':
    main()
