class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        string_ = []
        elem = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name_ in self.file_names:
            with open(name_, 'r', encoding="utf-8") as file:
                for line in file:
                    line_ = line.lower()
                    for i in elem:
                        line_ = line_.replace (f"{i}", "")
                    string_ += line_.split()
                    all_words[name_] = string_
        return all_words

    def find(self, word:str):
        result = {}
        word_ = word.lower()
        for file, words in self.get_all_words().items():
            if words.count(word_):
                result[file] = words.index(word_)+1 # индекс работает с 0
        return result


    def count(self, word):
        result = {}
        word_ = word.lower()
        for file, words in self.get_all_words().items():
            if words.count(word_):
                result[file] = words.count(word_)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего