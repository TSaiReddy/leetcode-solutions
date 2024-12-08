function compress(chars) {
  let i = 0;
  let pointer = 0;
  let charLen = chars.length;

  while (i < charLen) {
    let count = 0;
    let char = chars[i];
    while (i < charLen && char === chars[i]) {
      count++;
      i++;
    }
    chars[pointer] = char;
    pointer++;

    if (count > 1) {
      let strCount = String(count);

      for (let k = 0; k < strCount.length; k++) {
        chars[pointer] = strCount[k];
        pointer++;
      }
    }
  }

  return pointer;
}

// console.log(compress(["a", "a", "b", "b", "c", "c", "c"]));
console.log(
  compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
);
// console.log(compress(["a"]));
