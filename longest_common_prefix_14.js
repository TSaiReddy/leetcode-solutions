function longestCommonPrefix(strs) {
  let i = 0;
  let prefix = strs[0] || "";

  while (i < prefix.length) {
    for (let str of strs) {
      if (str[i] !== prefix[i]) {
        return prefix.slice(0, i);
      }
    }
    i++;
  }
  return prefix.slice(0, i);
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog", "racecar", "car"]));
console.log(longestCommonPrefix(["abab", "aba", ""]));
console.log(longestCommonPrefix([""]));
