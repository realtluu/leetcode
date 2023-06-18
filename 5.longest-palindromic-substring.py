#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        substr =""
        longest = ""
        j=0           #j means how many repeated characters

        for i, char in enumerate(s):
            substr += char

            if ( (i+1)<len(s) ):
                if (s[i+1]==char):   #repeating character
                    j+=1    
                else:         #start finding symmetry
                    n=1                    
                    while ( (i-j-n)>=0 ):
                        if ( (i+n)<len(s) ):

                            if ( s[i-j-n] == s[i+n]):   #found symmetry
                                substr = s[i-j-n] + substr + s[i+n]
                                n+=1
                            else:
                                break
                        else:
                            break
                    if (len(substr) > len(longest)):
                        longest = substr
                    substr=""
                    j=0
                    
            if (len(substr) > len(longest)):
                longest = substr
        return longest
        
# @lc code=end