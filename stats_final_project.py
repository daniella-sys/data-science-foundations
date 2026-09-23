import numpy as np

# Рядки — Філії (Філія 1, Філія 2, Філія 3, Філія 4)
# Стовпчики — Дні (Пн, Вт, Ср, Чт, Пт, Сб)
gym_data = np.array([
    [1.2, 1.5, 1.3, 1.6, 1.8, 2.0],       # Філія 1 (стабільна)
    [0.8, 0.9, 12.5, 0.8, 1.0, 1.1],      # Філія 2 (викид у Ср — 12.5!)
    [2.5, 2.8, 2.6, 3.0, 3.2, 3.5],       # Філія 3 (велика відвідуваність)
    [1.0, 1.1, 1.0, 1.2, 1.3, 1.5]        # Філія 4 (невелика затишна філія)
])

total_visitors= np.sum(gym_data) #Сумарна сума всіх відвідувачів 
total_std = np.std(gym_data) #Відхилення по всій матриці

#Порівняння стійкості метрик по філіях
branch_means = np.mean(gym_data, axis=1) #Середнє арифметичне для кожних 4 філій
branch_medians = np.median(gym_data, axis=1)
print(f"Медіана для філії 2: {branch_medians[1]:.2f}") #Медіана для філії 2 оскільки вона по індексу 1 по рахунку з 0 тому і 0
print(f"Середнє арифметичне значення філії 2: {branch_means[1]:.2f}")

#Нормалізація (центрування) даних філій через keepdims=True
branch_medians_2d = np.median(gym_data, axis=1, keepdims=True)
normalized_gym = gym_data - branch_medians_2d #BroadCasting

#Аналіз навантаження по днях для всієї мережі(усіх філій)
daily_total = np.sum(gym_data, axis=0)

#Вивід 
print("Сумарна сума всіх відвідувачів ", total_visitors)
print("Відхилення по всій матриці", total_std)
print(f"Результат знаходження медіани з виводом у вигляді стовпця: {np.round(branch_medians_2d, 2)}")
print("Результат обчислення двох матриць:", normalized_gym)
print(f"Навантаження по днях для всієї мережі: {np.round(daily_total, 2)}")
