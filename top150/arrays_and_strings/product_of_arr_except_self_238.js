function productExceptSelf(nums) {
  const result = [1];

  for (let i = 1; i < nums.length; i++) {
    result.push(nums[i - 1] * result[i - 1]);
  }

  let right = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= right;
    right *= nums[i];
  }

  return result;
}

console.log(productExceptSelf([1, 2, 3, 4])); //[24,12,8,6]

[1, 2, 6, 24][(24, 6, 4, 1)];
