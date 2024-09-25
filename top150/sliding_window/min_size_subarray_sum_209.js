function minSubArrayLen(target, nums) {
  let left = 0;
  let curSum = 0;
  let minWindow = Infinity;

  for (let right = 0; right < nums.length; right++) {
    curSum += nums[right];

    while (curSum >= target) {
      minWindow = Math.min(minWindow, right - left + 1);
      curSum -= nums[left];
      left++;
    }
  }

  return minWindow === Infinity ? 0 : minWindow;
}

console.log(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]));
console.log(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]));
