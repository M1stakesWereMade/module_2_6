def single_root_words(root_word, *other_words):
    same_words = []
    
    root_word_lower = root_word.lower()
    other_words_lower = [word.lower() for word in other_words]
    
    for word in other_words_lower:
        if root_word_lower in word or word in root_word_lower:
            same_words.append(word) 
    
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
