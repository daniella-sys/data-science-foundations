#примусове задання типу при створенні(dtype), зміна уже існуючого типу 
#імпорт бібліотеки
import numpy as np
float_arr= np.array([5, 12, 45, 100], dtype=float)
print(float_arr)
print(float_arr.dtype)


str_arr = np.array(["10", "20", "30", "40"])
#Конвертуємо у цілі числа
int_arr = str_arr.astype(int)
print("Тип даних рядок:", str_arr)
print("Тип даних цілі числа:", int_arr)
print(int_arr + 5)
