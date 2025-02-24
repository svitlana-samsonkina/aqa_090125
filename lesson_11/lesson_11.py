
def second_in_line(long_long_text:str, word:str):
    index = long_long_text.find(word)
    assert index != -1, f"{word} not found in text"
    index_2 = long_long_text.find(word, index + 1)
    return index_2

long_txt = "hour after hour. And when the middle of the afternoon came, from being"
word = "Tom"
print(second_in_line(long_txt, word))