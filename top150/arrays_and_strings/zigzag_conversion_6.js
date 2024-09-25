function convert(s, numRows) {
  if (numRows === 1) return s;
  const arr = Array.from({ length: numRows }, () => "");

  let count = 0;
  let inc = true;
  for (const ele of s) {
    arr[count] += ele;
    if (inc && count >= 0 && count < numRows - 1) {
      count++;
    } else {
      count--;
      inc = false;
    }
    if (count === 0) inc = true;
  }

  return arr.join("");
}

console.log(convert("PAYPALISHIRING", 3));
console.log(convert("AB", 1));
