#Практика з np.array()
import numpy as np
#Одновимірні масиви (Вектори)
list = [150, 300, 450, 600]

#конвертую його в масив(Numpy)
prices = np.array(list)

#Векторна математика:
discounted_prices = prices * 0.9
print(f"Початкові ціни на товари: {prices}")
print(f"Ціни уже зі знижкою: {discounted_prices}")

#Двовимірні масиви (Матриці)
matrix = np.array([
    [21, 1500, 5],
    [35, 2800, 12],
    [42, 3100, 8]
])
