class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) {
            return false;
        }
        let dict_s = {};
        let dict_t = {};
        for (let i=0; i<s.length; i++) {
            dict_s[s[i]] = 1 + (dict_s[s[i]] ?? 0)
            dict_t[t[i]] = 1 + (dict_t[t[i]] ?? 0)
        }
        return Object.keys(dict_s).every(key => dict_t.hasOwnProperty(key) && dict_s[key] === dict_t[key])
    }
}
