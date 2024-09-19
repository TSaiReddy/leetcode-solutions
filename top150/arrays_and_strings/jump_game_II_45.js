function jump(nums) {
  let totalJumps = 0;
  let curStep = 0;
  let maxSteps = 0;

  for (let i = 0; i < nums.length - 1; i++) {
    curStep = Math.max(curStep, i + nums[i]);

    if (maxSteps === i) {
      maxSteps = curStep;
      totalJumps++;
    }
  }
  return totalJumps;
}

console.log(jump([2, 3, 1, 1, 4]));
console.log(jump([2, 4, 1, 2, 3, 1, 1, 2]));
