#примусове задання типу при створенні(dtype), зміна уже існуючого типу 
#імпорт бібліотеки
import numpy as np
prices = np.array([19.99, 5.50, 10.35, 99.99])
rounded_prices = prices.astype(int)
print(f"Масив з числами типу(float): {prices}")
print(f"Масив чисел з типом(int): {rounded_prices}")

raw_data = np.array([0, 1, 5, 0, -3])
bool_arr = raw_data.astype(bool)
print(f"Масив з числами типу(int): {raw_data}")
print(f"Масив з числами типу(bool): {bool_arr}")

flags = np.array([True, False, True, True], dtype=int)
print(f"Примусове задання типу: {flags}")
print(f"Визначення суми цього масиву:", flags.sum())
