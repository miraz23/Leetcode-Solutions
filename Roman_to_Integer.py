#Link: https://leetcode.com/problems/roman-to-integer/

#Using list(Not Optimized)
'''
class Solution(object):
    def romanToInt(self, s):
        queries = [['I',1], ['V',5], ['X',10], ['L',50], ['C', 100], ['D',500], ['M',1000]]
        
        sum = 0
        values = []

        for i in range(0, len(s)):
            for roman, num in queries:
                if s[i] == roman:
                    values.append(num)

        for i in range(1, len(values)):
            if values[i-1] >= values[i]:
                sum += values[i-1]
            else: 
                sum -= values[i-1]

        return sum + values[len(values)-1]


        return values
                
'''

#Using dict(Optimized)
class Solution(object):
    def romanToInt(self, s):
        queries = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        sum = 0
        prev = queries[s[0]]

        for i in range(1, len(s)):
            current =  queries[s[i]]

            if prev >= current:
                sum += prev
            else:
                sum -= prev
            
            prev = current

        return sum + queries[s[len(s)-1]]
                
        