small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print('task 1')
unique_elements = set(small_list)
print("Унікальні елементи:", unique_elements)
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print('task 2')
average = sum(small_list) / len(small_list)
print(f"Середнє арифметичне: {average}")
# task 3. Перевірте, чи є в списку big_list дублікати
print("task 3")
print("Список:", big_list)
unique_set = set(big_list)
print("Список унікальних чисел:",unique_set)
has_duplicates = len(big_list) > len(unique_set)
print("Чи є дублікати в списку?", "Так" if has_duplicates else "Ні")
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("task 4")
max_key = max(add_dict)
print("Ключ з максимальним значенням:", max_key)
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("task 5")
print("Оригінальний словник:", add_dict)
inverted_dict = {value: key for key, value in add_dict.items()}
print("Перевернутий словник:", inverted_dict)
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("task 6")
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + "," + str(value)
    else:
        sum_dict[key] = value
print("Об'єднаний словник:", sum_dict)
# task 7.
print("task 7")
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars = set(line)
print("Множина всіх символів:", unique_chars)
# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("task 8")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
# logical_difference_1 = set_1 - set_2
# print("Елементи в set_1, але не в set_2:", logical_difference_1)
# logical_difference_2 = set_2 - set_1
# print("Елементи в set_2, але не в set_1:", logical_difference_2)
# logical_union = logical_difference_1.union(logical_difference_2)
# print("Об'єднана множина елементів, що не є спільними:", logical_union)
print("Сума елементів, що не є спільними:", sum(set_1 ^ set_2))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("task 10")

age_groups = {}
for name, age in person_list:
    age_range = f"{age // 10 * 10}-{age // 10 * 10 + 9}"
    if age_range not in age_groups:
        age_groups[age_range] = []
    age_groups[age_range].append(name)

print("Словник з віковими діапазонами:", age_groups)