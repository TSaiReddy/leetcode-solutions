function reverse(arr, start, end) {
  while (start < end) {
    [arr[start], arr[end]] = [arr[end], arr[start]];
    start++;
    end--;
  }
  return arr;
}

function rotate(nums, k) {
  k = k % nums.length;

  // Reverse Array
  reverse(nums, 0, nums.length - 1);

  // Reverse from 0 to K elements
  reverse(nums, 0, k - 1);

  // Reverse from K to End
  reverse(nums, k, nums.length - 1);

  return nums;
}

console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
