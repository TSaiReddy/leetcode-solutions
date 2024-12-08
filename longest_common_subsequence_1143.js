function longestCommonSubsequence(text1, text2) {
  let left = 0;
  let right = 0;
  while (left < text2.length - 1) {
    while (right < text1.length - 1) {
      if (text1[right] === text2[left]) break;
      right++;
    }
    if (right === text1.length - 1) return left;
    left++;
  }
  return left;
}

console.log(longestCommonSubsequence("abcde", "ace"));
console.log(longestCommonSubsequence("abc", "abc"));
console.log(longestCommonSubsequence("abc", "def"));
