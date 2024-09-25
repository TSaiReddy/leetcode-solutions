function maxArea(height) {
  let left = 0;
  let right = height.length - 1;

  let maxWater = 0;

  while (left < right) {
    leftHeight = height[left];
    rightHeight = height[right];
    let minHeight = Math.min(leftHeight, rightHeight);

    maxWater = Math.max(maxWater, minHeight * (right - left));

    if (leftHeight > rightHeight) {
      right--;
    } else {
      left++;
    }
  }
  return maxWater;
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
