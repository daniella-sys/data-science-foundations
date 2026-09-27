#ЧАСТИНА 1 Заключного проекту 
import numpy as np

#Генерація даних
sales1 = np.random.default_rng(seed=42)
sales = sales1.integers(100, 1000, size=30) #Масив
print("Генерація чисел від 100 до 1000 повторний запуск дає точно такі ж числа:", sales)

#Фільтрація та Булева маска
high_sales_mask = sales > 700
high_sales = sales[high_sales_mask]
print(f"Кількість днів там де ціна перевевищувала 700 грн: {len(high_sales)}")

print("Початковий масив sales:", sales)
