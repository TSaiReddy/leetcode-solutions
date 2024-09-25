function threeSum(nums) {
  if (!nums || nums?.length < 2) return result;

  const triplets = [];

  nums = nums.sort();

  for (let i = 0; i < nums.length - 2; i++) {
    // skips duplicate iteration
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum > 0) right--;
      else if (sum < 0) left++;
      else {
        triplets.push([nums[i], nums[left], nums[right]]);

        // skips duplicates
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      }
    }
  }
  return triplets;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
