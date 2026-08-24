#np.array()
#імпорт бібліотеки
import numpy as np
#Дослідження атрибутів масивів NumPy (.shape, .dtype, .ndim)
vector_arr = np.array([345, 278, 1, 8989, 42]) #Дослідження одновимірного масиву (Вектор)
print('\n Вектор: \n', vector_arr)
print('Вимірність масиву(його .ndim)', vector_arr.ndim)
print('Його shape:', vector_arr.shape)
print('Його тип даних:', vector_arr.dtype)

#Дослідження двовимірного масиву (Матриця)
matrix_arr = np.array([
    [1, 10.5, 3],
    [4, 5, 6]
])
print('\n Матриця: \n', matrix_arr)
print('Вимірність матриці(її .ndim)', matrix_arr.ndim)
print('Матриці shape:', matrix_arr.shape)
print('Її тип даних:', matrix_arr.dtype)


