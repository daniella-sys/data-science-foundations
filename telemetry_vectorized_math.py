#Нормалізація та обробка телеметрії серверів
import numpy as np 
# Сирі показники навантаження CPU з 4 серверів (%)
raw_cpu = np.array([45.0, 80.0, 15.0, 95.0])

#Віднімання (-):
calibrated_cpu = raw_cpu - 5.0

#Ділення (/):
normalized_cpu = calibrated_cpu / 100

#Піднесення до степеня (**):
squared_errors = normalized_cpu ** 2

#Множення (*):
projected_cpu = normalized_cpu * 1.2

#Додавання (+):
final_cpu = projected_cpu + 0.05

#Вивід 
print(calibrated_cpu, normalized_cpu, squared_errors, final_cpu)
