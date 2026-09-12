

#Data Pipeline для аналітики фінтех-платформи
import numpy as np
server_1 = np.arange(1, 13) #1 рядок на 12 елементів бо 13 не включно 
server_2 = np.arange(13, 25) #1 рядок на 12 елементів 25 не включно 

#Зміна розмірності та автоматичний розрахунок
s1_grid_c = server_1.reshape((3, 4), order='C')
s2_grid_f = server_2.reshape((3, -1), order='F')
print("Розмірність матриці 1:", s1_grid_c.shape)
print("Розмірність матриці 2:", s2_grid_f.shape)

#Об'єднання серверних даних
all_servers_v = np.vstack((s1_grid_c, s2_grid_f)) #об'єднання по вертикалі
fees = np.array([[0.1], [0.2], [0.15]]) 
s1_enriched = np.hstack((s1_grid_c, fees)) #по горизонталі s1 та fees  (fees створений вектор)
all_servers_h = np.concatenate((s1_grid_c, s2_grid_f), axis=1) #s1_grid_c та s2_grid_f по горизонталі

#Вивести розмірність 
print("Розмірність масиву:", all_servers_v.shape)
print("Розмірність масиву:", s1_enriched.shape)
print("Розмірність масиву:", all_servers_h.shape)

#Підготовка до експорту та аналіз пам'яті
export_copy = all_servers_v.flatten() #створили незалежну копію масиву яка не змінює основний масив
export_view = all_servers_v.ravel() #створили проекцію яка не витрачає память але змінює оригінальний масив
print("Незалежна копія масиву all_servers_v:", export_copy )
print("Створена проекція, яка не витрачає пам'ять та змінює оригінальний масив:", export_view)
print("Оригінальний масив all_servers_v:", all_servers_v)
