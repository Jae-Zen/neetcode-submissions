class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = "";
        for (let string of strs) {   //O(n)
            const length = String(string.length);
            res += length + "#" + string;
        }
        return res
    }

    decode(str) {
        const res = [];
        let start = 0;
        for (let i=0; i<str.length; i++) {
            if (str[i] === "#") {
                const length = parseInt(str.slice(start, i));
                const string = str.slice(i + 1, i + 1 + length);
                res.push(string);
                start = i + 1 + length;
                i = start;
            }
        }
        return res
    }
}
