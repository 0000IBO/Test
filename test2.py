def  clean_word(word):
    return word.strip().lower()
def get_vowels_in_word(word):
    vowel_str = "aeiou"
    vowels_in_word = ""
    for ch in word:
        if ch in vowel_str:
            vowels_in_word+=ch
    return vowels_in_word
#main program
data_file = open("words_alpha.txt","r")

for word in data_file:
    word = clean_word(word)
    if len(word) <=5:
        continue
    vowels_in_word = get_vowels_in_word(word)
    if vowels_in_word == "aeiou":
        print(word)
data_file.close()