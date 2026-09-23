import numpy as np

# Рядки — Сервери (Сервер 1, Сервер 2, Сервер 3)
# Стовпчики — Години (Година 1, Година 2, Година 3, Година 4)
server_load = np.array([
    [120, 125, 118, 122],      # Сервер 1 (стабільне навантаження)
    [ 50,  55, 950,  52],      # Сервер 2 (аномальний викид 950 на 3-й годині!)
    [300, 310, 305, 315]       # Сервер 3 (високе навантаження)
])

#Агрегація по всій матриці
total_sum = np.sum(server_load) #Обчислення сумарної кількості оброблених запитів серверами за певний час 
total_std = np.std(server_load) #Відхилення по всій матриці 

#Аналіз по СЕРВЕРАХ
mean_servers = np.mean(server_load, axis=1) #Середнє навантаження по всьому сервері
median_servers = np.median(server_load, axis=1) #Медіана по всьому сервері за всі години навантаження

#Аналіз по ГОДИНАХ
sum_servers = np.sum(server_load, axis=0) #Сумарне навантаження на всю систему

server_median_2d = np.median(server_load, axis=1, keepdims=True)
centered_load = server_load - server_median_2d #Спрацює BroadCasting 

#Вивід 
print("Cумарна кількість оброблених запитів серверами за весь час роботи:", total_sum:.2f)
print("Відхилення матриці:", total_std:.2f)
print(f"Середнє навантаження по всьому сервері: {np.round(mean_servers, 2)}")
print(f"Медіана по всьому сервері за всі години навантаження: {np.round(median_servers, 2)}")
print(f"Сумарне навантаження на всю систему: {np.round(sum_servers, 2)}")
print(f"Медіана кожного з серверів, але значення у вигляді стовпця: {np.round(server_median_2d, 2)}")
print("Результат BroadCasting:", centered_load)


