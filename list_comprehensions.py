#генератори списків 
track_streams = [12500, 3200, 45000, 890, 1500, 67000, 2300, 9800, 11200, 410] #list

#Фільтрація хітів
hits = [stream for stream in track_streams if stream >= 10000]

#фільтрація underground
underground = [stream for stream in track_streams if stream < 1000]

#зміна даних
k_streams = [stream/1000 for stream in track_streams]

#вивід 
print(f"Хіти: {hits}")
print(f"З меншою кількістю прослуховувань: {underground}")
print(f"У тисячах: {k_streams}")
