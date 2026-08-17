#базові функції
daily_plays = [450, 1200, 8900, 300, 15000, 80, 2100]
#кількість днів 
print(f"Кількість днів: {len(daily_plays)}")
#загальна сума 
total = sum(daily_plays)
print(f"Загальна сума: {total}")
#мінімальне та максимальне значення 
min_plays = min(daily_plays)
max_plays = max(daily_plays)
print(f"Мінімальне значення: {min_plays}")
print(f"Максимальне значенн: {max_plays}")

#створення власних функцій
def analyze_album(durations):
    total = sum(durations)
    count = len(durations)
    print(f"Альбом містить {count} треків загальною тривалістю {total} хв")

#виклик функції
album_tracks = [2.5, 3.1, 4.0, 2.8]
analyze_album(album_tracks)

def calculate_earnings(streams):
     #streams (кількість відтворень).
     income = streams * 0.005 #дохід
     if income >= 50:
        status ="Прибутковий"
     else:
        status = 'Початковий'
return (f"Дохід: ${income} | Статус: {status}")

track1_info = calculate_earnings(1200)
track2_info = calculate_earnings(3000)
print(track1_info)
print(track2_info)

def check_track_status(title, plays):
    if plays >= 10000:
        status = "Топ-хіт"
    else:
        status = "Звичайний трек"   
    return (f"Трек {title} має статус {status}")

track1 = check_track_status("Flowers", 15000)
track2 = check_track_status("Night Drive", 200)
print(track1)
print(track2)

def get_playlist_stats(playlist_name, streams):
    total_streams = sum(streams)
    max_streams = max(streams)
    return f"Плейлист '{playlist_name}': всього {total_streams} стрімів, рекорд — {max_streams}"

rock_hits = [1500, 8900, 24000, 5100]
stats = get_playlist_stats("Rock Classics", rock_hits)
print(stats)
