// Greedy Approach

function canJump(nums) {
  let len = nums.length - 1;
  let curIdx = nums.length - 2;

  if (nums[0] === 0 && len >= 1) return false;
  if (len === 0) return true;

  while (curIdx >= 0) {
    let canReachLast = curIdx + nums[curIdx];
    if (canReachLast >= len) len = curIdx;
    curIdx--;
  }
  return len === 0;
}

console.log(canJump([2, 3, 1, 1, 4])); // true
console.log(canJump([3, 2, 1, 0, 4])); // false
console.log(canJump([0, 1])); // false
console.log(canJump([0])); // true
console.log(canJump([2, 5, 0, 0])); // true
console.log(canJump([1, 2, 0, 1])); // true
console.log(canJump([2, 0, 0])); // true
