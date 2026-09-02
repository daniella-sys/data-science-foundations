#Симуляція тестового датасету користувачів
#імпорт бібліщтеки 
import numpy as np
rng_fixed = np.random.default_rng(seed=42) #створює генератор випадкових чисел з фіксованими числами 
ages = rng_fixed.integers(18, 66, size=6)
print("Генерація випадкових чисел від 18 до 65 з стабільною фіксацією:", ages)

#Генерація ймовірностей / відсотків
conversion_rates = rng_fixed.random(4)
print("Генерація 4 випадкових чисел від 0 до 1:", conversion_rates)

#Симуляція реальних параметрів                                 #Об'єкт rng_fixed — це просто єдиний генератор (джерело випадковості), 
heights = rng_fixed.normal(loc=175, scale=7, size=(2,3))    # а .integers(), .random() та .normal() — це різні інструменти (методи) цього генератора.
print(heights)

#Аналіз згенерованих даних
print(ages.mean())
print(heights.sum())
