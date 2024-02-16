function findDuplicate(nums) {
  let tortoise = nums[0];
  let hare = nums[0];
  while (true) {
    tortoise = nums[tortoise];
    hare = nums[nums[hare]];

    if (tortoise === hare) {
      break;
    }
  }

  tortoise = nums[0];
  while (tortoise !== hare) {
    tortoise = nums[tortoise];
    hare = nums[hare];
  }
  return hare;
}

console.log(findDuplicate([1, 3, 2, 4, 2]));
