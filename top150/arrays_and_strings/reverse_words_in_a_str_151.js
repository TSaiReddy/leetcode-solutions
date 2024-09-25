function reverseWords(s) {
  const str = s.trim();

  const words = [];
  let word = "";

  for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      if (word.length > 0) {
        words.push(word);
        word = "";
      }
    } else word += str[i];
  }

  if (word !== "") words.push(word);
  return words.reverse().join(" ");
}

console.log(reverseWords("the sky is blue"));
console.log(reverseWords("  hello    world  "));
