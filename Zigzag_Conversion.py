"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
		#test condition for only 1 row
        if numRows==1:
            return s 
		#store all zig-zag rows in alphabets
        alphabets = [[] for _ in range(numRows)]
        counter = 0
        for i in range(n):
			#if reaches top, downwards zigzag patter
            if counter == (numRows-1):
                val = -1
			#if reaches botton, upwards zigzag pattern
            if counter == 0:
                val = 1
				
			#add values to respective rows
            alphabets[counter].append(s[i])
            counter = counter + val
        #join values of all rows and return string
        return ("".join(["".join(k) for k in alphabets]))
