#Система аналізу серверних метрик (Server Health Dashboard)
#імпорт бібліотеки 
import numpy as np
server_ids = np.array([101, 102, 103])
print("Тип даних масиву:", server_ids.dtype)

#Ініціалізація буферів пам'яті
status_matrix = np.zeros((3, 4))
weight_coefficients = np.ones(3)

#Генерація часових шкалок
hours = np.arange(0, 25, 6)
load_percentages = np.linspace(0, 100, 5)

#Симуляція випадкових метрик
rng_fixed = np.random.default_rng(seed=42) #генератор випадкових чисел для методів
ping_ms = rng_fixed.integers(10, 101, size=3) #3 цілих чисел від 10 до 100
cpu_load = rng_fixed.normal(loc=60, scale=15, size=3)

#Підсумковий аналіз metrics
print(cpu_load.mean())
print(ping_ms.max())
print(hours.sum())
