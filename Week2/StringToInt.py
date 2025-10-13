class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_digits = []
        i = 0
        #first_nondigit_seen = False
        s = s.lstrip(' ') #strip leading spaces
        if len(s) == 0:
            return 0

        negative = False # deal with signs 
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                negative = True
            s = s[1:]

        s = s.lstrip('0') #strip leading 0's 

        integer = 0
        while i < len(s):
            char = s[i]
            if not char.isdigit():
                break
            if char.isdigit():
                #list_digits.append(int(char))   
                integer = integer * 10 + int(char)
            i += 1
        
        if negative: 
            integer = integer * -1
            
        #rounding cases:
        if integer < -2 ** 31:
            integer = -2 ** 31
        if integer > 2 ** 31 - 1:
            integer = 2 ** 31 - 1
        return integer
        
