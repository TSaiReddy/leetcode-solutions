function isSubsequence(s, t) {
  let sLen = 0;
  let tLen = 0;

  while (tLen < t.length) {
    if (s[sLen] === t[tLen]) {
      sLen++;
    }
    tLen++;
  }

  return sLen === s.length;
}

console.log(isSubsequence("abc", "ahbgdc"));
console.log(isSubsequence("axc", "ahbgdc"));
console.log(isSubsequence("b", "abc"));
