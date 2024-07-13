/**
 * @param {string} s
 * @return {number}
 */

function lengthOfLongestSubstring(s) {
  let hash = {};
  let maxLen = 0;
  let l = 0;

  for (let r = 0; r < s.length; r++) {
    const char = s[r];
    if (hash.hasOwnProperty(char) && hash[char] >= l) {
      l = hash[char] + 1;
    }

    hash[char] = r;
    maxLen = Math.max(maxLen, r - l + 1);
  }
  return maxLen;
}

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("dvdf"));
