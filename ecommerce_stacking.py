#Об'єднання аналітичних даних E-commerce
import numpy as np

saturday_sales = np.array([[501, 1200],
                           [502, 3400],
                           [503, 850]])

sunday_sales = np.array([[504, 2100],
                         [505, 4300]])

#Додавання нових транзакцій по вертикалі
weekend_sales = np.vstack((saturday_sales, sunday_sales))
print("Розмірність масиву:", weekend_sales.shape)

#Збагачення даних новими метриками по горизонталі
extra_metrics = np.array([[10, 80],
                          [15, 0],
                          [5, 80]])
full_saturday = np.hstack((saturday_sales, extra_metrics))
print("Розмірність масиву:", full_saturday.shape)

