#Аналіз даних інтернет-магазину
import numpy as np

# Сирий список продажів у гривнях (4 продукти x 5 днів)
raw_sales = [
    [12000, 15000, 8000, 22000, 18000],  # Laptop
    [5000,  7000,  6000, 4000,  9000],   # Phone
    [3000,  0,     2500, 3100,  0],      # Tablet
    [8000,  9500,  7000, 11000, 10500]   # Monitor
]

sales = np.asarray(raw_sales) #перетворення звичайного масиву в масив NumPy

#Векторна індексація та зрізи
wentheday = sales[1, 2] #виведе продажі телефона у середу
tuzden = sales[0, :] #усі продажі ноутбуків за весь тиждень
Friday = sales[:, 4] #вивід усіх продажів у п'ятницю 
submatrices_output = sales[0:2, 0:3] #виведе продажі ноутбуків та телефонів у пн-вт-ср 
print("Продажі телефонів у середу:", wentheday)
print("Всі продажі ноутбуків за весь тиждень:", tuzden)
print("Вивід усіх продажів у п'ятницю:", Friday)
print("Продажі ноутбуків та телефонів у пн-вт-ср:", submatrices_output)

#Аналітика та перевірка (np.any, np.all, np.count_nonzero)
print("Продаж продукту за тиждень що перевищив 20 000:", np.any(sales > 20000))
print("Кількість успішних продажів:", np.count_nonzero(sales > 0))

#Boolean Masking + Логічні оператори (&, |, ~)
mask1 = (sales >= 5000) & (sales <= 12000)
print("Усі продажі від 5 000 до 12 000:", sales[mask1])
mask2 = ~(sales == 0) #Не нульові продажі
print(sales[mask2])

#Розширена категоризація (np.select)
conditionss = [
    sales >= 15000, #умова 1
    sales >= 5000, #умова 2
    sales > 0 #умова 3
]

categories = ['High Sale', 'Medium Sale', 'Low Sale']
results = np.select(conditionss, categories, default="No Sale")
print("Результат фільтрації по умовах:", results)
