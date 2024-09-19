function longestCommonPrefix(strs) {
  let char = strs[0] || "";

  let i = 0;
  while (i < char.length) {
    for (const str of strs) {
      if (str[i] !== char[i]) {
        return char.slice(0, i);
      }
    }
    i++;
  }
  return char.slice(0, i);
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
