function removeDuplicates(nums) {
  let swapIdx = 1;
  let curIdx = 1;
  let count = 1;

  while (curIdx < nums.length) {
    if (nums[curIdx - 1] === nums[curIdx]) {
      count++;
    } else {
      count = 1;
    }

    if (count <= 2) {
      nums[swapIdx] = nums[curIdx];
      swapIdx++;
    }
    curIdx++;
  }

  return swapIdx;
}

console.log(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]));
// console.log(removeDuplicates([1, 1, 1, 2, 2, 3]));
