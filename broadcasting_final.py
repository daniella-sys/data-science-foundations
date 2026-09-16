import numpy as np
base_rates = np.array([50.0, 100.0, 150.0]) #створили вектор 1х3

#перетворення рядка на стовпчик 
rates_col = base_rates[:, np.newaxis] #означає взяти всі рядки і зробити +1 стовпчик 

#Створення ще одного вектора 1х4
load_factors = np.array([1.0, 1.2, 1.5, 2.0])

#Вбудований Broadcasting: через різницю розмірності підлаштує матрицю меншу під більшу
brocs = rates_col * load_factors 

print("Отримана матриця певної розмірності:", brocs.shape)
