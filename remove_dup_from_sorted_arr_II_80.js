function removeDuplicates(nums) {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    if (element === nums[i + 1]) {
      if (count > 1) {
        nums.splice(i, 1);
        nums.push(element);
      }
      count++;
    } else {
      count = 0;
    }
  }
  return nums;
}

console.log(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]));
