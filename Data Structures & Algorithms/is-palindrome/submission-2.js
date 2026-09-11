class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (!this.is_alnum(s[i])) {
                i++;
                continue
            }
            if (!this.is_alnum(s[j])) {
                j--;
                continue
            }
            if (s[j].toLowerCase() !== s[i].toLowerCase()) {
                return false
            }
            i++
            j--
        }
        return true
        
    }

    is_alnum(char) {
        const val = char.charCodeAt(0);
        return ((val >= 97 && val <= 122) 
                || (val >= 65 && val <= 90) 
                || (val >= 48 && val <=57)
                )

    }
}
