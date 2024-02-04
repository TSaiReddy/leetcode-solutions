function removeDuplicates(nums) {
  let lastSwapIdx = 1;
  let curIdx = 1;
  let count = 1;

  while (curIdx < nums.length) {
    if (nums[curIdx - 1] === nums[curIdx]) {
      count++;
    } else {
      count = 1;
    }

    if (count <= 2) {
      nums[lastSwapIdx] = nums[curIdx];
      lastSwapIdx++;
    }
    curIdx++;
  }
  return nums.slice(0, lastSwapIdx);
}

// console.log(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]));
console.log(removeDuplicates([1, 1, 1, 2, 2, 3]));
