print("Task 01-03")
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where" —— said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '—— "so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("Task 04")
square_black_sea = 436402
square_sea_of_azov = 37800
square_total = int(square_black_sea + square_sea_of_azov)
output = (f"Загальна площа Чорного та Азовського морів становить {square_total} км2.")
print(output)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("Task 05")
# Дано
total_goods = 375291
first_and_second = 250449
second_and_third = 222950

# Розв'язок
second = first_and_second + second_and_third - total_goods
first = first_and_second - second
third = second_and_third - second

# Результат
print(f"Кількість товарів на першому складі: {first}")
print(f"Кількість товарів на другому складі: {second}")
print(f"Кількість товарів на третьому складі: {third}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("Task 06")
payment_per_month = 1179
duration_of_payment = 1.5 * 12
computer_cost = payment_per_month * duration_of_payment
print(f"Вартість комп'ютера: {computer_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Task 07")
remainder_a = 8019%8
remainder_b = 9907%9
remainder_c = 2789%5
remainder_d = 7248%6
remainder_e = 7128%5
remainder_f = 19224%9
print(f"Остача від ділення 8019 на 8 дорівнює {remainder_a} \n"
      f"Остача від ділення 9907 на 9 дорівнює {remainder_b} \n"
      f"Остача від ділення 2789 на 5 дорівнює {remainder_c} \n"
      f"Остача від ділення 7248 на 6 дорівнює {remainder_d} \n"
      f"Остача від ділення 7128 на 5 дорівнює {remainder_e} \n"
      f"Остача від ділення 19224 на 9 дорівнює {remainder_f} \n"
      )

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("Task 08")
pizza_large = 4 * 274
pizza_middle = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_cost = pizza_large + pizza_middle + juice + cake + water
print(f"Загальна вартість замовлення: {total_cost} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("Task 09")
total_photos = 232
photos_per_page = 8
pages_needed = total_photos // photos_per_page
print(f"Кількість сторінок, необхідна для вклеювання всіх фото: {pages_needed}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("Task 10")
distance_km = 1600
fuel_per_100km = 9
tank_capasity = 48

total_fuel_needed = (distance_km / 100) * fuel_per_100km
refuels_needed = total_fuel_needed // tank_capasity

print(f"Необхідно бензину для подорожі: {total_fuel_needed} літрів")
print(f"Кількість заправок, необхідна для подорожі: {int(refuels_needed)} рази")