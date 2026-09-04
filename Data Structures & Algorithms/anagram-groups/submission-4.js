class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const records = {};
        for (const string of strs) {
            const freq_arr = new Array(26).fill(0);
            for (const char of string) {
                const char_i = char.charCodeAt(0) - 'a'.charCodeAt(0);
                freq_arr[char_i]++;
            }
            const key = String.fromCharCode(...freq_arr);
            (records[key] ??= []).push(string);
        }
        return Object.values(records)
    }
}
