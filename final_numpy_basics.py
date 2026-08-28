#Заключний мініпроєкт: «Аналітичний модуль обробки сирих даних»
#імпорт бібліотеки
import numpy as np
raw_activity = np.array(["15", "0", "42", "100", "0"])
print("Початковий тип даних: ", raw_activity.dtype)
#зміна типу на int 
activity_arr = raw_activity.astype(int)
print("Теперішній тип даниx: ", activity_arr.dtype)
total = sum(activity_arr)
print("Загальна сума елементів: ", total)


coefficients = np.array([1.99, 0.50, 3.75, 12.10]) #Робота з дробовими показниками та відкидання дробової частини
scores = coefficients.astype(int)
print("Початковий масив float:", coefficients)
print("Масив після відкидання дробової частини:", scores)


#Дослідження матриці та явне задання типів
status_matrix = np.array([
    [True, False, True],
      [False, True, True]
], dtype= int)
print('Кількість вимірів:', status_matrix.ndim)
print('Кількість елементів:', status_matrix.shape)
print('Тип даних у матриці:', status_matrix.dtype)
total1 = status_matrix.sum()
print("Загальна сума усіх елементів у матриці:", total1)

