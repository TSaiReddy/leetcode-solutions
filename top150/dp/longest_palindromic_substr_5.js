function longestPalindrome(s) {
  const strLen = s.length;
  if (strLen <= 1) return s;

  let result = "";
  let curLen = 0;

  function palindrome(left, right) {
    while (left >= 0 && right < strLen && s[left] === s[right]) {
      if (right - left + 1 > curLen) {
        result = s.substring(left, right + 1);
        curLen = right - left + 1;
      }
      left--;
      right++;
    }
  }

  for (let i = 0; i < strLen; i++) {
    palindrome(i, i);
    palindrome(i, i + 1);
  }

  return result;
}

console.log(longestPalindrome("babad"));
