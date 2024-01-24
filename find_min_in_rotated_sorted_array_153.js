function findMin(nums) {
  if (nums.length <= 1) {
    return nums[0];
  }
  const mid = Math.floor(nums.length / 2);

  const left = findMin(nums.slice(0, mid));
  const right = findMin(nums.slice(mid));
  return left > right ? right : left;
}

// console.log(findMin([3, 4, 5, 1, 2]));
// console.log(findMin([4, 5, 6, 7, 0, 1, 2]));
// console.log(findMin([3, 1, 2]));
// console.log(findMin([2, 1]));
console.log(findMin([2, 3, 4, 5, 1]));
