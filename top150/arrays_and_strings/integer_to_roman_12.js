function intToRoman(num) {
  const hash = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];

  let result = "";
  for (const [key, value] of hash) {
    while (num >= key) {
      result += value;
      num -= key;
    }
  }
  return result;
}

console.log(intToRoman(3749));
