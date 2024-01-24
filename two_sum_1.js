function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    const diff = target - element;
    if (map.has(diff)) {
      return [map.get(diff), i];
    }
    map.set(element, i);
  }
}

// console.log(twoSum([2, 7, 11, 15], 9));
// console.log(twoSum([3, 2, 4], 6));
// console.log(twoSum([3, 3], 6));
