function reverseVowels(s) {
  s = s.split("");
  const set = new Set(["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]);
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    const sLeft = set.has(s[left]);
    const sRight = set.has(s[right]);

    if (sLeft && sRight) {
      [s[left], s[right]] = [s[right], s[left]];
      left++;
      right--;
    }
    if (!sLeft) left++;
    if (!sRight) right--;
  }
  return s.join("");
}
console.log(reverseVowels("IceCreAm"));
