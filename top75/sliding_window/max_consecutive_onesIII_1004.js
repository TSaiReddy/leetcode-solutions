/**
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

function longestOnes(nums, k) {
  let left = 0;
  let max = 0;

  for (let right = 0; right < nums.length; right++) {
    console.log(nums[right], k, max);
    if (nums[right] === 0) k--;

    while (k < 0) {
      if (nums[left] === 0) k++;
      left++;
    }
    max = Math.max(max, right - left + 1);
  }
  return max;
}

console.log(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2));
console.log(
  longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
);
