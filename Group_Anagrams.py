# Link: https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram[sorted_word].append(word)

        return list(anagram.values())