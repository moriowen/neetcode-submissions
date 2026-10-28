class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if len(word) == index:
                return node.end

            char = word[index]

            if char == ".":
                # search every children 
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
            
            if char not in node.children:
                return False
            return dfs(index + 1, node.children[char])
        return dfs(0, self.root)
