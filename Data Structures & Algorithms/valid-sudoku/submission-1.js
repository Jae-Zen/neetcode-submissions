class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const rows = new Map();
        const cols = new Map();
        const squares = new Map();

        for (let r=0; r<9; r++) {
            for (let c=0; c<9; c++) {
                const num = board[r][c];
                if (num === '.') continue;
                const squareKey = `${Math.floor(r / 3)},${Math.floor(c / 3)}`
                if (rows.has(r) && rows.get(r).has(num) ||
                    cols.has(c) && cols.get(c).has(num) ||
                    squares.has(squareKey) && squares.get(squareKey).has(num)
                ) {
                    return false;
                }

                if (!rows.has(r)) rows.set(r, new Set());
                if (!cols.has(c)) cols.set(c, new Set());
                if (!squares.has(squareKey)) squares.set(squareKey, new Set());

                rows.get(r).add(num);
                cols.get(c).add(num);
                squares.get(squareKey).add(num);
            }
        }
        return true
    }
}