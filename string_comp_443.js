function compress(chars) {
  let currentLetter = null;
  let currentLetterCount = 0;
  let indexToPut = 0;

  for (let i = 0; i < chars.length + 1; i++) {
    const char = chars[i];

    if (char !== currentLetter) {
      if (currentLetter !== null) {
        chars[indexToPut] = currentLetter;
        indexToPut += 1;
        if (currentLetterCount > 1) {
          const countInStr = `${currentLetterCount}`;
          for (let digit of countInStr) {
            chars[indexToPut] = digit;
            indexToPut += 1;
          }
        }
      }

      currentLetter = char;
      currentLetterCount = 1;
    } else {
      currentLetterCount += 1;
    }
  }

  return [indexToPut, chars];
}

console.log(
  compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
);
