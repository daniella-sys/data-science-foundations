#Генерація матриць із нулів, одиниць, діапазонів 
#Імпорт бібліщтеки 
import numpy as np
empty_buffer = np.zeros(6) #створення вектора з 6 нулів 
print("Тип даних у векторі:", empty_buffer.dtype) #за замовчуванням ставить тип float

active_servers = np.ones((3,4), dtype=int)
print("Матриця:", active_servers)
print("Кількість елементів у матриці:", active_servers.shape)
print("Сума елементів у матриці:", active_servers.sum())

scores_draft = np.zeros((4), dtype=int)
print(scores_draft)
#зміна першого та останнього елементу на числа
scores_draft[0] = 10 #змінили перший елемент на 10
scores_draft[-1] = 50 #змінили останній елемент на 50
print("Оновленний масив:", scores_draft)
