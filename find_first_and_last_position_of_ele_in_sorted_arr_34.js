function searchRange(nums, target) {
  function binary(start, end) {
    if (start > end) {
      return [-1, -1];
    }

    const mid = Math.floor((start + end) / 2);

    if (nums[mid] === target) {
      let left = mid;
      while (left > 0 && nums[left - 1] === target) {
        left--;
      }
      let right = mid;
      while (right < nums.length - 1 && nums[right + 1] === target) {
        right++;
      }
      return [left, right];
    }

    if (nums[mid] > target) {
      return binary(start, mid - 1);
    }

    if (nums[mid] < target) {
      return binary(mid + 1, end);
    }
  }

  if (nums.length === 0) {
    return [-1, -1];
  }

  return binary(0, nums.length - 1);
}

console.log(searchRange([5, 7, 7, 8, 8, 10], 8));
// console.log(searchRange([5, 7, 7, 8, 8, 10], 6));
// console.log(searchRange([1], 1));
// console.log(searchRange([], 3));
// console.log(searchRange([1, 2, 3], 3));
