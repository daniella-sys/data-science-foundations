#Очищення та обробка рядка
raw_data = "   Drake - Hotline Bling ; 1,200,000 ; HIP-HOP   "
#очищення від зайвих пробілів та розбиття на частини(список)
clean = raw_data.strip().split(';')

#очистити від зайвих пробілів першу частину за індексом [0]
track_info = clean[0].strip()

#видалити кому очистити від пробілів і перетворити на число за індексом [1]
streams_count = int(clean[1].replace(",", "").strip())

#очистити від пробілів, переведи в нижній регістр за індексом [2]
genre = clean[2].strip().lower()

#вивід 
print(track_info)
print(streams_count)
print(genre)




