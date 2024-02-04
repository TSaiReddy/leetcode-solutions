// Moore's Voting Algorithm

function majorityElement(nums) {
  let majority = 0;
  let votes = 0;

  for (const num of nums) {
    if (votes === 0) {
      majority = num;
      votes = 1;
    } else if (majority !== num) {
      votes--;
    } else {
      votes++;
    }
  }
  return majority;
}

console.log(majorityElement([3, 2, 3]));
