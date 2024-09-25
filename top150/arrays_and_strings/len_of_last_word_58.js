function lengthOfLastWord(s) {
  let len = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    if (len > 0 && s[i] === " ") return len;
    if (s[i] !== " ") len++;
  }
  return len;
}

console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("   fly me   to   the moon  "));
