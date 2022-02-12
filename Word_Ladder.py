"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        n = len(beginWord)
        
        queue = [beginWord]
        num_words = 1
        seen = set()
        seen.add(beginWord)
        while queue:
            new_queue = []
            num_words += 1
            for word in queue:
                for i in range(n):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in dictionary:
                                if new_word == endWord:
                                    return num_words
                                if new_word not in seen:
                                    seen.add(new_word)
                                    new_queue.append(new_word)
            queue = new_queue
        return 0
