function removeDuplicates(nums) {
  let curIdx = 0;
  let swapIdx = 0;

  while (swapIdx < nums.length) {
    if (nums[curIdx] !== nums[curIdx + 1]) {
      curIdx++;
      swapIdx++;
    } else {
      while (swapIdx < nums.length) {
        if (nums[swapIdx] !== nums[swapIdx + 1]) {
          [nums[curIdx], nums[swapIdx]] = [nums[swapIdx], nums[curIdx]];
          curIdx++;
        }
        swapIdx++;
      }
    }
  }
  return curIdx;
}

console.log(removeDuplicates([1, 1, 2]));
// console.log(removeDuplicates([1, 2, 3]));
// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));
