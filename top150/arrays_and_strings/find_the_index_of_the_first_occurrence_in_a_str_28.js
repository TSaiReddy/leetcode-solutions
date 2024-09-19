function strStr(haystack, needle) {
  let needleLen = needle.length;
  let haystackLen = haystack.length;

  if (needleLen > haystackLen) return -1;

  let i = 0;
  while (i < haystackLen) {
    let j = 0;
    while (j < needleLen && haystack[j + i] === needle[j]) {
      j++;
    }
    if (j === needleLen) {
      return i;
    }
    i++;
  }
  return -1;
}

console.log(strStr("leetcode", "leeto"));
console.log(strStr("saadbutsad", "sad"));
console.log(strStr("mississippi", "issip"));
