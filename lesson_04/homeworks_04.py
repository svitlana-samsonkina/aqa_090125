adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("task 01")
new_line_added = adwentures_of_tom_sawer.replace("\n", " ")
print(new_line_added)
# task 02 ==
""" Замініть .... на пробіл
"""
print("task 02")
removed_extra_dots = adwentures_of_tom_sawer.replace("....", " ").replace("\n", " ")
print(removed_extra_dots)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("task 03")
removed_extra_dots = adwentures_of_tom_sawer.strip().replace(" ....", "").replace("\n", " ")
print(removed_extra_dots)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("task 04")
count_h_symbol = adwentures_of_tom_sawer.find("h")
print(f"Кількість букв 'h' в тексті: {count_h_symbol}")

# task 05 
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("task 05")
split_text = adwentures_of_tom_sawer.split()
count_uppercase_words = sum(1 for word in split_text if word[0].isupper()) #тут мені допоміг chatgpt
print(f"Кількість слів, що починаються з Великої літери: {count_uppercase_words}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("task 06")
adwentures_of_tom_sawer_updated = adwentures_of_tom_sawer.replace(" ....", "").replace("\n", " ")
start = adwentures_of_tom_sawer_updated.find("Tom")
next_tom = adwentures_of_tom_sawer_updated.find("Tom", start+1)
print(adwentures_of_tom_sawer_updated[next_tom:])

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("task 07")
import re
removed_extra_dots = adwentures_of_tom_sawer.replace(" ....", "").replace("\n", " ")
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s*', removed_extra_dots)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task 08")
import re
removed_extra_dots = adwentures_of_tom_sawer.replace(" ....", "").replace("\n", " ")
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s*', removed_extra_dots)
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
lowercase_fourth_sentence = fourth_sentence.lower()
print(f"Четверте речення з тексту перетворене в нижній регістр: {lowercase_fourth_sentence}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("task 09")
import re
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s*', adwentures_of_tom_sawer.strip())
starts_with_phrase = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print(f"Чи починається якесь речення з 'By the time'? {'Так' if starts_with_phrase else 'Ні'}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("task 10")
import re
removed_extra_dots = adwentures_of_tom_sawer.replace(" ....", "").replace("\n", " ")
adwentures_of_tom_sawer_sentences = re.split(r'[.!?]\s*', removed_extra_dots.strip())
adwentures_of_tom_sawer_sentences = [sentence for sentence in adwentures_of_tom_sawer_sentences if sentence]
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(f"Останнє речення: {last_sentence}")
words_in_last_sentence = last_sentence.split()
print(f"Кількість слів в останньому реченні: {len(words_in_last_sentence)}")