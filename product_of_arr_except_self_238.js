function productExceptSelf(nums) {
  let result = [];

  let sum = 1;
  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    result.push(sum);
    sum *= element;
  }

  sum = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    const element = nums[i];
    const val = result[i] * sum === -0 ? 0 : result[i] * sum;
    result[i] = val;
    sum *= element;
  }

  return result;
}

console.log(productExceptSelf([1, 2, 3, 4]));
