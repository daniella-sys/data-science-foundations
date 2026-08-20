#Фінальний проєкт: "Аналізатор стримінгової статистики"
track_streams = [12500, 3200, 45000, 890, 1500, 67000, 2300, 9800, 11200, 410]
def analyze_album_data(streams): #функція
    #базова статистика 
    count = len(streams) #кількість елементів у масиві 
    total = sum(streams) #загальна сума елементів у масиві 
    min_streams = min(streams) #мінімальне максимальне значення 
    max_streams = max(streams)
    #лічильники для того аби профільтрувати по категоріям масив 
    hits = 0 
    seredni = 0
    underground = 0
    #фільтрація (if/elif/else + for)
    for analyze in streams:
        if analyze >= 10000:
            hits += 1 #якщо умова правдива то кількість хітів додається 
        elif 1000 <= analyze <= 9999:
            seredni += 1
        else:
            underground += 1
    #вивід
    print(f"Статистика: кількість елементів: {count} загальна сума: {total} мінімальне та максимальне значення: {min_streams} {max_streams}")
    print(f"Хіти: {hits} Середні: {seredni} Інші: {underground}")

#передаємо аргумент і викликаємо функцію 
analyze_album_data(track_streams)


