function rob(nums) {
  let memo = new Array(nums.length).fill(undefined);

  function robFrom(i) {
    if (i >= nums.length) {
      return 0;
    }

    if (memo[i] !== undefined) {
      return memo[i];
    }

    let ans = Math.max(nums[i] + robFrom(i + 2), robFrom(i + 1));
    memo[i] = ans;
    return ans;
  }

  return robFrom(0);
}

console.log(rob([2, 7, 9, 3, 1]));
// console.log(rob([2, 1, 1, 2]));
// console.log(rob([1, 2]));
