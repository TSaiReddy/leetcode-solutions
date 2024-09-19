function merge(nums1, m, nums2, n) {
  let pointer1 = 0;
  let pointer2 = 0;

  while (pointer2 < n) {
    if (pointer1 >= m + pointer2 || nums1[pointer1] > nums2[pointer2]) {
      nums1.splice(pointer1, 0, nums2[pointer2]);
      nums1.pop();
      pointer2++;
    }

    pointer1++;
  }

  return nums1;
}

console.log(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3));
