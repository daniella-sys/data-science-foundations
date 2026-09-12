
#Preprocessing пикселів для алгоритму Computer Vision
import numpy as np
frame_a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
frame_b = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125])

img_a = frame_a.reshape((3, 4), order='C')
img_b = frame_b.reshape((3, 4), order='F')
print("Розмірність масиву:", img_a.shape)
print("Розмірність масиву:", img_b.shape)

#Склеювання кадрів (Панорама та Пачка кадрів)
vertical_panorama = np.vstack((img_a, img_b))
print("Розмірність матриці:", vertical_panorama.shape)

horizontal_panorama = np.hstack((img_a, img_b))
print("Розмірність матриці:", horizontal_panorama.shape)

alpha = np.array([[255], [255], [255]])
img_a_rgba = np.concatenate((img_a, alpha), axis=1)
print("Розмірність масиву:", img_a_rgba.shape)

#Конвертація для нейромережі та безпека пам'яті
nn_input_copy = vertical_panorama.flatten() #Створює незалежну копію яка не впливає на оригінальний масив + сплющує і робить 1D вектор
nn_input_view = vertical_panorama.ravel() #займає менше пам'яті і змінює основний масив
nn_input_copy[0] = 0 #зміна найпершого елементу
nn_input_view[-1] = 255 #зміна останнього елементу в масиві
print("Незалежна копія масиву nn_input_copy:", nn_input_copy)
print("Створена проекція, яка не витрачає пам'ять та змінює оригінальний масив:", nn_input_view)
print('Оригінальний масив vertical_panorama:', vertical_panorama)
