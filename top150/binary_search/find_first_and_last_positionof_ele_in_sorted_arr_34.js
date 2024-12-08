function searchRange(nums, target) {
  const result = [];
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] >= target) {
      if (nums[mid] === target) {
        if (nums[mid - 1] === target) {
          result.push(mid - 1);
          result.push(mid);
        } else {
          result.push(mid);
          result.push(mid + 1);
        }
      } else {
        console.log(right, "ll");
        left = mid;
      }
    } else {
      left = mid + 1;
    }
  }

  return result;
}

console.log(searchRange([5, 7, 7, 8, 8, 10], 8));
