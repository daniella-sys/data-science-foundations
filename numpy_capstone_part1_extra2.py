#ЧАСТИНА 1/практична частина
import numpy as np

#Генерація даних:
gen_int = np.random.default_rng(seed=200)
delivery_times = gen_int.integers(15, 60, size=30) #Масив

#Фільтрація та Булева маска:
late_deliveries_mask = delivery_times > 45
late_deliveries = delivery_times[late_deliveries_mask]

#Вивід у консоль:
print("Початковий масив:", delivery_times)
print(f"Кількість доставок, які запізнились: {len(late_deliveries)}")
print("Запізнілі доставки:", late_deliveries)
