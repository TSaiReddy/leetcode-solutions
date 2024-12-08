function gcdOfStrings(str1, str2) {
  if (str1 + str2 !== str2 + str1) return "";

  const divisor = gcd(str1.length, str2.length);
  return str1.slice(0, divisor);

  function gcd(a, b) {
    if (b === 0) return a;
    return gcd(b, a % b);
  }
}

console.log(gcdOfStrings("ABCABC", "ABC"));
