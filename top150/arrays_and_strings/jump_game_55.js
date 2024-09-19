// Greedy

function canJump(nums) {
  let goal = nums.length - 1;

  for (let i = nums.length - 1; i >= 0; i--) if (i + nums[i] >= goal) goal = i;

  if (goal === 0) return true;
  else return false;
}

console.log(canJump([2, 3, 1, 1, 4]));
