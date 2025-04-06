# Link: https://leetcode.com/problems/letter-tile-possibilities/

class Solution(object):
    def numTilePossibilities(self, tiles):
        def backtrack(counter):
            total = 0
            for ch in counter:
                if counter[ch] == 0:
                    continue

                total += 1
                counter[ch] -= 1
                total += backtrack(counter)
                counter[ch] += 1
                
            return total

        counter = Counter(tiles)
        return backtrack(counter)