function twoSum(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const sum = numbers[left] + numbers[right];
    if (sum < target) {
      left += 1;
    } else if (sum > target) {
      right -= 1;
    } else {
      return [left, right];
    }
  }
}
