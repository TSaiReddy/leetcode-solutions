function removeElement(nums, val) {
  if (nums.length === 1 && nums[0] === val) {
    return 0;
  }

  let curIdx = 0;
  let lastSwapIdx = nums.length - 1;

  while (curIdx <= lastSwapIdx) {
    if (nums[curIdx] === val) {
      while (lastSwapIdx > curIdx && nums[lastSwapIdx] === val) {
        lastSwapIdx--;
      }
      [nums[curIdx], nums[lastSwapIdx]] = [nums[lastSwapIdx], nums[curIdx]];
      lastSwapIdx--;
    }
    curIdx++;
  }
  return lastSwapIdx + 1;
}

// console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2, 2], 2));
// console.log(removeElement([4, 5], 5));
// console.log(removeElement([1], 1));
// console.log(removeElement([2], 3));
// console.log(removeElement([3, 3], 3));
// console.log(removeElement([3, 3], 3));
