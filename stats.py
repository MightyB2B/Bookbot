def word_count(text):
    get_num_words = 0
    split_words = text.split()
    get_num_words = len(split_words)

    return get_num_words

def letter_count(text):
    letters = {}
    lowercase_words = text.lower()
    for letter in lowercase_words:
        if letter in letters:
            letters[letter] +=1
        else:
            letters[letter] = 1

    return letters

def sort_by_number(item_dict):
    value = item_dict["num"]
    return value

def sorted_letter_count(letters):
    dict_letter_count = []
    for letter, num in letters.items():
        if letter.isalpha():
            temp_letter_count = {"char": letter, "num": num}  
            dict_letter_count.append(temp_letter_count)      
    dict_letter_count.sort(reverse=True, key=sort_by_number)    
    return dict_letter_count


