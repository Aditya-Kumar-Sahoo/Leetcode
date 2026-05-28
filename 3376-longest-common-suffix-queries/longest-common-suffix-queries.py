class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # insert reversed container words
        for i, word in enumerate(wordsContainer):
            rev = word[::-1]
            node = root

            # update root answer
            if len(word) < node.length:
                node.length = len(word)
                node.idx = i

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if len(word) < node.length:
                    node.length = len(word)
                    node.idx = i

        ans = []

        # process queries
        for word in wordsQuery:
            rev = word[::-1]
            node = root

            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.idx)

        return ans