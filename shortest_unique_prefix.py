"""

Shortest unique prefix 

Provided a list of words, for each word find the shortest unique prefix. 
You can assume a word will not be a substring of another word
(ie play and playing won't be in the same words list)

Example
Input: ['joma', 'john', 'jack', 'techlead']
Output: ['jom', 'joh', 'ja', 't']

"""

class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie: 
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
            curr_node.count += 1
    def unique_prefix(self, word):
        curr_node = self.root
        prefix = ''

        for c in word:
            if curr_node.count == 1:
                return prefix
            else:
                curr_node = curr_node.children[c]
                prefix += c
        return prefix

    
def shortest_unique_prefix(words):

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']