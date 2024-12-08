/**
 *
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

function findMaxAverage(nums, k) {
  let sum = 0;
  for (let i = 0; i < k; i++) sum += nums[i];

  let avg = sum / k;

  for (let i = 1; i < nums.length - k + 1; i++) {
    sum = sum - nums[i - 1] + nums[i + k - 1];

    avg = Math.max(avg, sum / k);
  }

  return avg;
}

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4));
