function firstMissingPositive(nums) {
  let isSmall = nums[0];
  let idx = 0;
  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    if (element < isSmall && element >= 0) {
      isSmall = element;
      idx = i;
    }
  }
  return idx + 1;
}

// console.log(firstMissingPositive([7, 8, 9, 11, 12]));
console.log(firstMissingPositive([3, 4, -1, 1]));
// console.log(firstMissingPositive([1, 2, 0]));
