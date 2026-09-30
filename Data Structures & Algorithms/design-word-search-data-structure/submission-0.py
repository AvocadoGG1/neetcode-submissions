class TrieNode:
    def __init__(self):
    
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


    def search(self, word: str) -> bool:
        def dfs(i, node):

            # Reaches end (successfully finding every char)
            if i == len(word):
                
                return node.word
            
            
            # Wildcard "."
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else: # Normal letter
                if word[i] not in node.children:
                    return False
                return dfs(i + 1, node.children[word[i]])

                
        return dfs(0, self.root)
        
    
