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
    print(same_words)

single_root_words('Samara', 'sam', 'ara', 'dad', 'well')