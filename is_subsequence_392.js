function isSubsequence(s, t) {
  if (s.length < 1) {
    return true;
  }
  let arr = t.split("");
  let subStr = false;
  let prevIdx = 0;
  for (let i = 0; i < s.length; i++) {
    const element = s[i];
    const curIdx = arr.indexOf(element);
    if (curIdx !== -1) {
      subStr = true;
      if (curIdx >= prevIdx) {
        arr = arr.slice(curIdx + 1);
        prevIdx = 0;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }
  return subStr;
}

// console.log(isSubsequence("ab", "baab"));
// console.log(isSubsequence("acb", "ahbgdc"));
console.log(isSubsequence("abc", "ahbgdc"));
