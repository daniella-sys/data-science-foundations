#Генерація матриць із нулів, одиниць, діапазонів 
#Імпорт бібліщтеки 
import numpy as np

hours = np.arange(0, 25, 2) #числа від 0 до 24 (25 не включається) парні числа
print(hours)
print("Тип даних у масиві:", hours.dtype)

time_stamps = np.linspace(0, 10, 5) # від 0 до 10 дай мені 5 чисел
print(time_stamps)
print("Сума усіх чисел:", time_stamps.sum())

arr_step = np.arange(0, 11, 2.5) #Числа від 0 до 10 з різницею прогресії на +2.5
arr_count = np.linspace(0, 10, 5)
print(arr_step)
print(arr_count)

#Шкала годин вимірювання
sensor_hours = np.arange(0, 25, 3) #числа від 0 до 24(число 25 не включається) і різниця прогресії +3
print(sensor_hours)
print("Загальна сума цих чисел:", sensor_hours.sum())

#Шкала навантаження для графіка
load_percent = np.linspace(0, 100, 5) #від 0 до 100(100 включається) розбиває 5 чисел в цьому проміжку
print("Початковий масив:", load_percent)
print("Тип даних цього масиву:", load_percent.dtype)

#Перевірка логіки
countdown = np.arange(10, 0, -1) #числа від 10 до 1 (0 не враховується) рахує числа назад
print(countdown)
