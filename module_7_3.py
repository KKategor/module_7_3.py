# Task "Найдёт везде"

class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        l = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding= 'utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in  punc:
                        line = line.replace(i, '')
                l = l + line
            all_words.update({self.file_names: l.split()})

        return all_words

    def find(self, word):
        dict = {}
        t = self.get_all_words()[self.file_names]
        for i in range(len(word)):
            if word.lower() == t[i]:
                dict.update({self.file_names: i + 1})
                return dict

    def count(self, word):
        dict = {}
        n = 0
        t = self.get_all_words()[self.file_names]
        dict.update({self.file_names: t.count(word.lower())})
        return dict



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего