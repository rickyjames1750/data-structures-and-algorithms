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
        # root pointing to a node 
        self.root = Node()
    def insert(self, word):
        curr_node = self.root
        # Loops through the characters of a word 
        for c in word:
            # if no children create new node 
            if c not in curr_node.children:
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
            # counter tells how many words gone through that node  
            curr_node.count += 1
    def unique_prefix(self, word):
        # Init our current node 
        curr_node = self.root
        # then return our prefix
        prefix = ''

        # Iteration again so if it is 1 then return the prefix 
        for c in word:
            if curr_node.count == 1:
                return prefix
            else:
                # Keep going and += add the character 
                curr_node = curr_node.children[c]
                prefix += c
        return prefix

    
def shortest_unique_prefix(words):
    # For a function we define the Trie()
    trie = Trie()

    for word in words:
        trie.insert(word)

    unique_pref = []
    # Loop through the words again 
    for word in words:
        unique_pref.append(trie.unique_prefix(word))

    return unique_pref

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
