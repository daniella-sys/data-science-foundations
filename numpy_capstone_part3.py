#ЧАСТИНА 3
import numpy as np

#Підготовка даних
gen_int = np.random.default_rng(seed=400)
gym_visitors = gen_int.integers(50, 300, size=28) #МАСИВ
gym_visitors_matrix = gym_visitors.reshape(4, 7)
week_5 = gen_int.integers(50, 300, size=7).reshape(1, 7)
full_visitors_schedule = np.vstack((gym_visitors_matrix, week_5))

#Статистика по всій матриці
total_suma = np.sum(full_visitors_schedule)
total_means = np.mean(full_visitors_schedule)
total_median = np.median(full_visitors_schedule)

#Аналіз по осях
total_suma_axis = np.sum(full_visitors_schedule, axis=1)
total_means_axis =np.mean(full_visitors_schedule, axis=0)

#Векторизація та Бродкастинг
boosted_visitors = full_visitors_schedule * 1.15

#Форматований вивід у консоль:
print("Початкова матриця:", full_visitors_schedule)
print("Загальна сума матриці, середнє арифметичне матриці, та медіана матрриці:", total_suma, total_means,total_median)
print("Сума по кожному тижню та середнє по кожному дня тижня:", total_suma_axis, total_means_axis)
print("Матриця після приросту на 15%:", boosted_visitors)
