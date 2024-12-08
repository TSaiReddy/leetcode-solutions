/**
 *
 * @param {number[]} gain
 * @returns {number}
 */

function largestAltitude(gain) {
  let max = 0;
  let curSum = 0;

  for (const height of gain) {
    curSum += height;
    max = Math.max(max, curSum);
  }
  return max;
}

console.log(largestAltitude([-5, 1, 5, 0, -7]));
