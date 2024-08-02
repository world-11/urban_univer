def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            if text[j-1:i+1] != '':
                yield text[j-1:i+1]


a = all_variants("abc")
for i in a:
    print(i)