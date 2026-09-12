
class PrefixTree:

    def __init__(self, isword=False):
        self.children = {}
        self.word = isword

    def insert(self, word: str) -> None:
        if len(word) == 1:
            if word not in self.children:
                new = PrefixTree(True)
                self.children[word] = new
            else:
                self.children[word].word = True
        
        else:
            first = word[0]
            toret = word[1:]

            if first not in self.children:
                new = PrefixTree()
                self.children[first] = new
                new.insert(toret)
            else:
                self.children[first].insert(toret)
            
        

    def search(self, word: str) -> bool:

        if len(word) == 1:
            if word in self.children:
                return self.children[word].word
            return False
        
        else:
            first = word[0]
            toret = word[1:]

            if first not in self.children:
                return False
            else:
                return self.children[first].search(toret)

    def startsWith(self, prefix: str) -> bool:
        
        if len(prefix) == 1:
            if prefix in self.children:
                return True
            return False
        
        else:
            first = prefix[0]
            toret = prefix[1:]

            if first not in self.children:
                return False
            else:
                return self.children[first].startsWith(toret)
        