# Link: https://leetcode.com/problems/convert-date-to-binary/

class Solution(object):
    def convertDateToBinary(self, date):
        year, month, day = date.split('-')
        bin_year = bin(int(year))[2:]
        bin_month = bin(int(month))[2:]
        bin_day = bin(int(day))[2:]
        return "{}-{}-{}".format(bin_year, bin_month, bin_day)