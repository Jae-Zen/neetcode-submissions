#Space O(n)
#Time O(n)

class Solution:
    def isPalindrome(self, s: str):
        string = ""
        for letter in s:
            if ((ord(letter) < 48) 
            or (57 < ord(letter) and ord(letter) < 65) 
            or (ord(letter) > 90 and ord(letter) < 97) 
            or (ord(letter) > 122)):
                continue
            
            string += letter.lower()

        length = len(string)
        for i in range(len(string) // 2):
            if string[i] != string[length-i-1]:
                print(i)
                return False

        return True
