#ЧАСТИНА 1/практична частина
import numpy as np

gen_num = np.random.default_rng(seed=100)
server_requests = gen_num.integers(200, 1000, size=30) #Масив

#Фільтрація та Булева маска:
critical_load_mask = server_requests > 800
critical_requests = server_requests[critical_load_mask]

#Вивід у консоль:
print("Початковий масив:", server_requests)
print(f"Кількість хвилин з шаленим навантаженням: {len(critical_requests)}")
print("Значення які перевищують > 800:", critical_requests)
