#Симуляція інтернет-магазину (E-Commerce)
#імпорт бібліотеки 
#Створити генератор випадкових чисел rng_shop з фіксованим seed=100
import numpy as np
rng_shop = np.random.default_rng(seed=100)
items_count = rng_shop.integers(1, 11, size=5)
print("Генерація випадкових цілих чисел від 1 до 10:", items_count)

#Персональна знижка
discounts = rng_shop.random(5)
print("Генерація 5 випадкових чисел від 0 до 1:", discounts)

#Сума чека покупців (.normal)                            #Об'єкт rng_fixed — це просто єдиний генератор (джерело випадковості), 
cart_totals = rng_shop.normal(loc=500, scale=50, size=5)   # а .integers(), .random() та .normal() — це різні інструменти (методи) цього генератора.
print(cart_totals)

#Аналіз даних
print(discounts.max())
print(cart_totals.mean())
