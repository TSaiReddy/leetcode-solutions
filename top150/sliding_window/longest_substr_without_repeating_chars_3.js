function lengthOfLongestSubstring(s) {
  const hash = new Set();
  let left = 0;
  let maxCount = 0;

  for (let right = 0; right < s.length; right++) {
    while (hash.has(s[right])) {
      hash.delete(s[left]);
      left++;
    }
    hash.add(s[right]);
    maxCount = Math.max(maxCount, right - left + 1);
  }
  return maxCount;
}

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
