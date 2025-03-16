# Link: https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution(object):
    def sortTheStudents(self, score, k):
        score.sort(key=lambda x: x[k], reverse=True)
        return score