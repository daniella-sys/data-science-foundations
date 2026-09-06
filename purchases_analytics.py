
# Сирі дані (звичайний список Python):
raw_purchases = [150, 0, 420, 1200, 80, 0, 310, 2500, 95]

purchases = np.asarray(raw_purchases) #перетворюємо звичайний список 

#Перевірка та підрахунок (np.any, np.all, np.count_nonzero)
print("Перевірка чи є один чек більший за 2000:", np.any(purchases > 2000))
print("Порахунок скільки було покупок де сума > 0:", np.count_nonzero(purchases > 0))

#Складна фільтрація (Boolean Masking + &, |, ~)
mask = (purchases > 100) & (purchases <= 500)
print(purchases[mask])

mask_1 = ~(purchases == 0)
print(purchases[mask_1])

#Категоризація через np.select()
conditions = [
    purchases >= 1000,   #умова №1
    purchases >= 300, #Умова №2
    purchases > 0
]
#розподіл по категоріях
categories = ["VIP Purchase", "Standard Purchase", "Small Purchase"]

results = np.select(conditions, categories, default="No Purchase")
print("Результат відбору:", results)
