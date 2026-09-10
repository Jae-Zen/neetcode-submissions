class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        for (let row of board) {
            const row_freq = {};  //check for each row
            for (let i=0; i<9; i++) {
                let num = row[i];
                if (num == '.') {
                    continue
                }
                if (row_freq[num] ?? 0 == '1') {
                    return false
                } else {
                    row_freq[num] = '1'
                }  
            }
        }
        
        for (let j=0; j<9; j++) {
            const column_freq = {};
            for (let i=0; i<9; i++) {
                let num = board[i][j];
                if (num === '.') {
                    continue
                } else if (column_freq[num] === '1') {
                    return false
                } else {
                    column_freq[num] = '1'
                }
            }
        }

        for (let boxRow=0; boxRow<9; boxRow+=3) {
            for (let boxCol=0; boxCol<9; boxCol+=3) {
                const boxFreq = {};
                for (let i=0; i<3; i++) {
                    for (let j=0; j<3; j++) {
                        const num = board[boxRow + i][boxCol + j];
                        if (num === '.') {
                            continue
                        } else if (boxFreq[num] ?? 0 == '1') {
                            return false
                        } else {
                            boxFreq[num] = '1';
                        }

                    }
                }
                
            }
        }
        return true

            
    }
}
