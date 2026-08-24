#np.array()
#імпорт бібліотеки
import numpy as np
#Автоматичне приведення типів 
#Змішування int та float
arr = np.array([10, 70, 30.4])
print(arr) #Виведе: [10. 70. 30.4] int стало float

#Змішування bool та int
bool_to_int_array = np.array([True, False, 28])
print(bool_to_int_array) #Виведе: [1 0 28]

#Додавання рядка (str)
str_array = np.array([10, 5678, 6578.3388, False, 'sdfxvghd2'])
print(str_array) #Виведе: ['10' '5678' '6578.3388' 'False' 'sdfxvghd2']


