/**
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s) {
  const strLen = s.length;

  if (strLen <= 1) return s;

  let res = "";
  let resLen = 0;

  function expandAroundCenter(left, right) {
    while (left >= 0 && right < strLen && s[left] === s[right]) {
      const curLen = right - left + 1;
      if (curLen > resLen) {
        res = s.substring(left, right + 1);
        resLen = curLen;
      }
      left--;
      right++;
    }
  }

  for (let i = 0; i < strLen; i++) {
    // Odd-length palindromes
    expandAroundCenter(i, i);

    // Even-length palindromes
    expandAroundCenter(i, i + 1);
  }

  return res;
}

console.log(longestPalindrome("babad"));
console.log(longestPalindrome("ac"));
