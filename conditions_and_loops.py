#if/elif/else
plays = 8500
if plays > 10000:
    status = "Хіт"
elif 1000 <= plays <= 10000:
    status = "Популярний"
else:
    status = "Андеграунд"
print(f"Статус треку: {status}")
#for
durations = [2.5, 3.1, 4.0, 2.8, 3.5]
total_time = 0
for time in durations:
    total_time += time
print(f"Загальна тривалість альбому: {total_time} хв")
#Умови + Цикли разом
streams = [450, 1200, 8900, 300, 15000, 80]
popular_count = 0
for count in streams:
    if count > 1000:
        print(f"Знайдено хіт: {count} відтворень")
        popular_count += 1

print(f"Всього популярних треків: {popular_count}")

#Умови
duration_sec = 215
if duration_sec < 120:
    category = "Інтро"
if 120 <= duration_sec <= 240:
    category = "Стандартний трек"
else: 
    category = 'Епічний'
print(f"Статус категорії: {category}");

#Цикли (for)
weekly_listeners = [1200, 1500, 980, 2100, 1800, 2300, 1100]
total_listeners = 0
for count_listeners in weekly_listeners:
    total_listeners += count_listeners
print(f"Загальна кількість: {total_listeners}")

#Умови + Цикли
ticket_prices = [150, 80, 200, 50, 120, 300, 90]
vip_total_income = 0
regular_tickets_count = 0
for prise_ticket in ticket_prices:
    if prise_ticket >= 150:
        vip_total_income += prise_ticket
    else:
        regular_tickets_count += 1
print(f"Дохід від VIP квитків: {vip_total_income} грн")
print(f"Кількість звичайних квитків: {regular_tickets_count} шт.")
