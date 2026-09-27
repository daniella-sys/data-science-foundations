#ЧАСТИНА 2
import numpy as np
#Генерація та Reshape
gen_int = np.random.default_rng(seed=300)
network_traffic = gen_int.integers(100, 500, size=24) #МАСИВ
traffic_matrix = network_traffic.reshape(4, 6)

#Створення та Stacking
extra_shift = gen_int.integers(100, 500, size=6)
extra_shift_matrix = extra_shift.reshape(1, 6)
full_traffic_matrix = np.vstack((traffic_matrix, extra_shift_matrix))

#Вивід у консоль:
print("Розмірність матриці:", full_traffic_matrix.shape)
print("Результат приєднання рядків по вертикалі(матриця):", full_traffic_matrix)
