#Аналітика рекламної кампанії (Ad Campaign Analytics)
#імпорт бібліотеки 
import numpy as np
campaign_ids = np.array([201, 202, 203, 204])
print("Тип даних у векторі:", campaign_ids.dtype)

#Ініціалізація буферів пам'яті
conversions_buffer = np.zeros((4, 5))
bid_multipliers = np.ones(4)

#Генерація діапазонів та шкал
days = np.arange(1, 32, 5)
budget_steps = np.linspace(100, 1000, 4)

#Симуляція випадкових метрик
rng_fixed = np.random.default_rng(seed=77) #генератор випадкових чисел для методів
clicks = rng_fixed.integers(50, 501, size=4)
ctr = rng_fixed.normal(loc=2.5, scale=0.5, size=4)

#Підсумковий аналіз metrics
print("Середнє значення:", ctr.mean())
print("Максимальне значення:", clicks.max())
print("Загальна сума згенерованих днів:", days.sum())
