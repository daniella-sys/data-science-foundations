
import numpy as np

# Температура повітря за тиждень (°C)
temps = np.array([18, 25, 31, 12, 0, 28, -3])

#Boolean Masking + Логічні оператори
#Створюємо булеву маску
mask1 = temps > 20 

#Фільтрація створює масив де лише ті елементи які відповідають умовам 
filther_temps = temps[mask1]
print("Масив елементів які відповідають умові:", filther_temps)

mask2 = (temps > 0) & (temps <= 25) #числа від 0 до 25(включно)
print(temps[mask2])

#Перевірка та підрахунок (np.any, np.all, np.count_nonzero)
print("Показує чи є хоча б один день з температурою < 0:", np.any(temps < 0))
print("Показує кількість елементів, що відповідають умові:", np.count_nonzero(temps > 20))

#Категоризація даних через np.select()
scores = np.array([42, 85, 93, 60, 74])

conditional = [
    #умова 1 
    scores >= 90,
    scores >= 60 #умова 2
]
choices = ["А(High)", "C(Medium)"]

result = np.select(conditional, choices, default="Low")
print("Результат наших умов та надань статусів:", result)

