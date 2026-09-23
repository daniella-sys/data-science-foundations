import numpy as np

# Рядки — Студенти (Студент 1, Студент 2, Студент 3, Студент 4)
# Стовпчики — Предмети (Математика, Фізика, Програмування)
scores = np.array([
    [80, 90, 70],   # Студент 1
    [60, 65, 70],   # Студент 2
    [95, 85, 90],   # Студент 3
    [75, 80, 85]    # Студент 4
])

#Обчислення середнього бала кожного студента
student_means = np.mean(scores, axis=1, keepdims=True) #Зліва направо обчислює середній бал студента вивід стовпцем 
#Broadcasting
centered_scores = scores - student_means

#Обчислення середнього бала по предметах
subject_means = np.mean(scores, axis=0) #Обчислення середнього балу з предмету за всіма студентами вивід вектором 

#Форматований вивід
print("Розмірність матриці:", student_means.shape)
print(f"Результат використання Broadcasting: {np.round(centered_scores, 2)}")
print(f"Середній бал по предметах: {np.round(subject_means, 2)}")
