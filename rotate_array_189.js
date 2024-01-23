function reverseArray(arr, start, end) {
  while (start < end) {
    [arr[start], arr[end]] = [arr[end], arr[start]];
    start++;
    end--;
  }
}

function rotate(nums, k) {
  k = k % nums.length;

  // Reverse the entire array
  reverseArray(nums, 0, nums.length - 1);

  // Reverse the first k elements
  reverseArray(nums, 0, k - 1);

  // Reverse the remaining elements
  reverseArray(nums, k, nums.length - 1);

  return nums;
}

// console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
// console.log(rotate([1, 2], 3));
// console.log(rotate([3, 2, 1], 4));
// console.log(rotate([-1, -100, 3, 99], 2));
