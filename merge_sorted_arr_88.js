function merge(nums1, m, nums2, n) {
  let left_pointer = m - 1;
  let right_pointer = n - 1;
  let num1_len = nums1.length - 1;

  while (right_pointer >= 0) {
    const element = nums2[right_pointer];

    if (left_pointer >= 0 && element > nums1[left_pointer]) {
      nums1[num1_len] = element;
      right_pointer--;
      num1_len--;
    } else if (left_pointer >= 0 && element < nums1[left_pointer]) {
      nums1[num1_len] = nums1[left_pointer];
      left_pointer--;
      num1_len--;
    } else {
      nums1[num1_len] = element;
      right_pointer--;
      num1_len--;
    }
  }
  return nums1;
}

console.log(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3));
