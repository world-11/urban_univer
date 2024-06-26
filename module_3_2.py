def single_root_words(root_word, *other_words):
    same_words = []
    m = root_word.lower()
    for i in range(len(other_words)):
        n = str(other_words[i])
        n = n.lower()
        if len(m) <= len(n) and n.count(m):
            same_words.append(other_words[i])
        elif len(m) > len(n) and m.count(n):
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
