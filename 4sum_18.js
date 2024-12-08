function fourSum(nums, target) {
  const arr = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 3; i++) {
    if (i > 0 && nums[i - 1] === nums[i]) continue;
    for (let j = i + 1; j < nums.length - 2; j++) {
      if (j > i + 1 && nums[j - 1] === nums[j]) continue;

      let left = j + 1;
      let right = nums.length - 1;
      while (left < right) {
        const sum = nums[i] + nums[j] + nums[left] + nums[right];
        if (sum > target) {
          right--;
        } else if (sum < target) {
          left++;
        } else {
          arr.push([nums[i], nums[j], nums[left], nums[right]]);

          // Avoid duplicates for `left` and `right`
          while (left < right && nums[left] === nums[left + 1]) left++;
          while (left < right && nums[right] === nums[right - 1]) right--;

          left++;
          right--;
        }
      }
    }
  }

  return arr;
}

console.log(fourSum([1, 0, -1, 0, -2, 2], 0));
