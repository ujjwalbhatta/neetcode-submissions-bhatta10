class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const st = s.split('').sort().join('')
        const tt = t.split('').sort().join('')
        return st == tt
    }
}
