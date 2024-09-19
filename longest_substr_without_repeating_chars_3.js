/**
 * @param {string} s
 * @return {number}
 */

function lengthOfLongestSubstring(s) {
  let hash = {};
  let maxLen = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    if (hash.hasOwnProperty(char) && hash[char] >= left) {
      left = hash[char] + 1;
    }

    hash[char] = right;
    maxLen = Math.max(maxLen, right - left + 1);
  }
  return maxLen;
}

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("dvdf"));
