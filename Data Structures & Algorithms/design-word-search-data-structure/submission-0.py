class WordDictionary:

    def __init__(self, isword = False):
        self.children = {}
        self.word = isword

    def addWord(self, word: str) -> None:
        if len(word) == 1:
            if word not in self.children:
                new = WordDictionary(True)
                self.children[word] = new
            else:
                self.children[word].word = True
        
        else:
            first = word[0]
            toret = word[1:]

            if first not in self.children:
                new = WordDictionary()
                self.children[first] = new
                new.addWord(toret)
            else:
                self.children[first].addWord(toret)

    def search(self, word: str) -> bool:
        if len(word) == 1:
            if word != '.' and word not in self.children:
                return False
            elif word == '.':
                for child in self.children:
                    if self.children[child].word:
                        return True
                return False
            else:
                return self.children[word].word
        
        else:
            first = word[0]
            toret = word[1:]

            if first != '.' and first not in self.children:
                return False
            elif first == '.':
                final = False
                for child in self.children:
                    final = (final or self.children[child].search(toret))
                return final
            else:
                return self.children[first].search(toret)




