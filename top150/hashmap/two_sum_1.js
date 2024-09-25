function twoSum(nums, target) {
  const hash = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;

    if (diff in hash) return [hash[diff], i];
    hash[num] = i;
  }
}

console.log(twoSum([2, 7, 11, 15], 9));
