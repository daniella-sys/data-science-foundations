#ЧАСТИНА 2
import numpy as np
#Генерація та Reshape
gen_int = np.random.default_rng(seed=400)
gym_visitors = gen_int.integers(50, 300, size=28) #МАСИВ
visitors_matrix = gym_visitors.reshape(4, 7)

#Створення та Stacking:
week_5 = gen_int.integers(50, 300, size=7)
week_5_matrix = week_5.reshape(1, 7)
full_visitors_schedule = np.vstack((visitors_matrix, week_5_matrix))

#Вивід у консоль:
print("Розмірність матриці:", full_visitors_schedule.shape)
print("Матриця:", full_visitors_schedule)
