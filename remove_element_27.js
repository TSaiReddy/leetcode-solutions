function removeElement(nums, val) {
  let pointer1 = 0;
  let pointer2 = nums.length - 1;

  while (pointer1 <= pointer2) {
    if (nums[pointer1] !== val) {
      pointer1++;
    } else if (nums[pointer1] === val) {
      while (nums[pointer2] === val) {
        pointer2--;
      }
      nums[pointer1] = nums[pointer2];
      pointer2--;
    } else {
      nums[pointer1] = nums[pointer2];
      pointer2--;
    }
  }
  return pointer1;
}
console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2, 2], 2));
console.log(removeElement([4, 5], 5));
