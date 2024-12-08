/**
 * @param {number} x
 * @returns {boolean}
 */

function isPalindrome(x) {
  x = String(x);
  let left = 0;
  let right = x.length - 1;

  while (left < right) {
    if (x[left] !== x[right]) return false;
    left++;
    right--;
  }
  return true;
}

console.log(isPalindrome(-121));
