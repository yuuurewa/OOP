class Film:
    films = []
    country = 'США'

    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration
        self.films.append(self)

film1 = Film('1+1', 11.5, 112)
film1.country = 'Франция'

film2 = Film('Хатико', 16, 85)

film3 = Film('Титаник', 200, 194)

film4 = Film('Интерстеллар', 165, 169)

film5 = Film('Достучаться до небес', 2.3, 87)
film5.country = 'Германия'

film6 = Film('Зеленая книга', 23,130)

film7 = Film('Балканский рубеж', 2.3,151)
film7.country = 'Россия'

film8 = Film('Лев', 12,118)
film8.country = 'Австралия'

film9 = Film('Достать ножи', 40,130)

film10 = Film('Чужой', 11,116)
film10.country = 'Великобритания'

film11 = Film('Аватар', 237,162)

film12 = Film('Джокер', 55,122)

Film.films.sort(key=lambda film: film.name)
for f in Film.films:
    print(f.name, f.country, sep=' - ')
print()
Film.films.sort(key=lambda film: film.country)
for f in Film.films:
    print(f.country, f.name, sep=' - ')

with open('oop1.txt', 'w+') as file:
    file.writelines(f'{i.name}, {i.country}, $ {i.price} млн, {i.duration} минут\n' for i in Film.films)
