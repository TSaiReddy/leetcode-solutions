/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function maxOperations(nums, k) {
  let left = 0;
  let count = 0;
  let right = nums.length - 1;
  nums.sort((a, (b) => a - b));

  while (left < right) {
    let sum = nums[left] + nums[right];
    if (sum === k) {
      left++;
      right--;

      count++;
    } else if (sum > k) right--;
    else left++;
  }

  return count;
}

console.log(maxOperations([1, 2, 3, 4], 5));
console.log(maxOperations([3, 1, 3, 4, 3], 5));
