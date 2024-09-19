// Moore's Voting Algorithm

function majorityElement(nums) {
  let majorityEle = nums[0];
  let count = 0;
  let idx = 0;

  while (idx < nums.length) {
    if (nums[idx] === majorityEle) {
      count++;
    } else {
      count--;
    }

    if (count === 0) {
      majorityEle = nums[idx];
      count++;
    }
    idx++;
  }
  return majorityEle;
}

console.log(majorityElement([3, 2, 3]));
