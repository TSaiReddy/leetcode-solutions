function containsNearbyDuplicate(nums, k) {
  let l = 0;
  const window = new Set();

  for (let r = 0; r < nums.length; r++) {
    const element = nums[r];
    if (r - l > k) {
      window.delete(nums[l]);
      l++;
    }

    if (window.has(element)) return true;
    window.add(element);
  }

  return false;
}

console.log(containsNearbyDuplicate([1, 2, 3, 1], 3));
console.log(containsNearbyDuplicate([1, 0, 1, 1], 1));
console.log(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2));
