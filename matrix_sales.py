#np.array()
#імпорт бібліотеки
import numpy as np
#Одновимірний масив (Вектор курсів валют)
price = [1000, 2500, 5000, 10000]
uah_amounts = np.array(price) #конвертувала
usd_amounts = uah_amounts / 41.5
print(f"Сума у гривнях: {uah_amounts}")
print(f"Сума у доларах: {usd_amounts}")

#Двовимірний масив (Матриця магазинів)
number_of_goods_sold = np.array([
    [5, 12, 20],
    [3, 8, 15],
    [10, 15, 30]
])
print(f"Кількість проданих товарів у трьох різних магазинах: {number_of_goods_sold}")

#Матрична математика
double_sales = number_of_goods_sold * 2 #продажі під час акції зросли вдвічі
print(f"Кількість проданих товарів після акції: {double_sales}")
