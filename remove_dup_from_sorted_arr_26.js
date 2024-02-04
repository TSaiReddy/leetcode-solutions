function removeDuplicates(nums) {
  let curIdx = 1;
  let lastSwapIdx = 1;
  while (curIdx < nums.length) {
    if (nums[curIdx - 1] !== nums[curIdx]) {
      nums[lastSwapIdx] = nums[curIdx];
      lastSwapIdx++;
    }
    curIdx++;
  }
  return nums.slice(0, lastSwapIdx);
}

console.log(removeDuplicates([1, 1, 2]));
// console.log(removeDuplicates([1, 2, 3]));
// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));
