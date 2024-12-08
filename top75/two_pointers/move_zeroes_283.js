function moveZeroes(nums) {
  let left = 0;
  let right = 0;
  while (right < nums.length) {
    if (nums[left] === 0 && nums[right] !== 0) {
      [nums[left], nums[right]] = [nums[right], nums[left]];
      left++;
    } else if (nums[left] !== 0) left++;
    right++;
  }

  return nums;
}

console.log(moveZeroes([0, 1, 0, 3, 12]));
console.log(moveZeroes([1, 0, 1]));
