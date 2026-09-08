#reshape() and .flatten()
#Реструктуризація даних пикселів зображення
raw_pixels= np.arange(16)
print("Створення вектора з 16 елементів починаючи з 0 до 15(показ розмірності масиву):", raw_pixels.shape)

# Перетворення на квадратну картинку (4 x 4)
image_4x4 = raw_pixels.reshape(4, 4)
print("Розмірність нашого масиву:", image_4x4.shape)

#Перетворення за допомогою магічного індексу -1
image_2x8 = raw_pixels.reshape(2, -1)
print("Розмірність нашого масиву:", image_2x8.shape)

#Сплющення даних назад у 1D-вектор
flat_pixels = image_4x4.flatten()
flat_pixels[0] = 999 #зміна першого елементу на 999
print("Сплющений масив 4х4:", flat_pixels)
print("Не сплющений масив 4х4:", image_4x4)

