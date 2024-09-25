function isPalindrome(s) {
  s = s.toLowerCase();

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (
      !(s[left].charCodeAt(0) >= 97 && s[left].charCodeAt(0) <= 122) &&
      !/\d/.test(s[left])
    ) {
      left++;
    } else if (
      !(s[right].charCodeAt(0) >= 97 && s[right].charCodeAt(0) <= 122) &&
      !/\d/.test(s[right])
    ) {
      right--;
    } else if (s[left] !== s[right]) {
      return false;
    } else {
      left++;
      right--;
    }
  }
  return true;
}

console.log(isPalindrome("race a car"));
console.log(isPalindrome("0P"));
