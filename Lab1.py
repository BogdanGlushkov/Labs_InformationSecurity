import matplotlib.pyplot as plt
import numpy as np

def encode(string, key):
    len_key = len(key)
    string += ' ' * (len_key - len(string) % len_key)
    matrix = [[] for _ in range(len_key)]
    for st in range(len(string) // len_key):
        for j, sub_key in enumerate(key):
            matrix[j].append(string[st * (len_key) + int(sub_key) - 1])
    return (''.join(''.join(i) for i in matrix))

# Пример использования
string = 'ВОТПРИМЕРШИФРАВЕРТИКАЛЬНОЙПЕРЕСТАНОВКИ----'
startKey = [5, 1, 4, 7, 2, 6, 3]
pltKey = ''
for num in range(0, len(startKey)):
    pltKey += str(startKey[num])
key = ''.join(map(str, [startKey.index(x)+1 for x in sorted(startKey)]))

encrypted_string = encode(string, key)

# Вывод результата в консоль
print(f"Исходная строка: {string}")
print(f"Ключ: {key}")
print(f"Зашифрованная строка: {encrypted_string}")


# Отображение раскрашенной матрицы с символами для шифра и добавление букв
matrix = [[string[i] for i in range(j, len(string), len(key))] for j in range(len(key))]
fig, ax = plt.subplots()
cax = ax.imshow([[ord(char) for char in row] for row in matrix], cmap='viridis', aspect='auto', interpolation='nearest')
plt.yticks(np.arange(len(key)), pltKey)
# plt.xticks(np.arange(len(string) // len(key)), np.arange(1, len(matrix)))
plt.xticks([])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        ax.text(j, i, matrix[i][j], ha='center', va='center', color='white')

plt.colorbar(cax)

plt.title("сообщение в прямоугольнике")
plt.show()