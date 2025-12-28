def get_num_words (text):
    word_count = 0
    word_list = []
    word_list = text.split()
    total_words = f"Found {len(word_list)} total words"
    return total_words

def character_count(text):
    letter_count = {}
    filter_text = text.lower()
    for letter in filter_text:
        if letter not in letter_count:
            letter_count[letter] = 0
            letter_count[letter] +=1
        else:
            letter_count[letter] += 1
    return letter_count

def letter_count(characters):
    total = []
    for char, num in characters.items():
        small_dict ={"char":char,"num":num}
        total.append(small_dict)
        total.sort(reverse=True, key=sort_on)
    return total

def sort_on(total):
    return total["num"]