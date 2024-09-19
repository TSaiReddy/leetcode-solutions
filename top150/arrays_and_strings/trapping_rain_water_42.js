// function trap(height) {
//   let maxLeft = 0;
//   let maxRight = 0;
//   const leftArr = [];
//   const rightArr = [];

//   for (let i = 0; i < height.length; i++) {
//     const j = -i - 1;
//     leftArr.push(maxLeft);
//     rightArr.unshift(maxRight);

//     maxLeft = Math.max(height[i], maxLeft);
//     maxRight = Math.max(height.at(j), maxRight);
//   }

//   let result = 0;
//   let i = 0;

//   while (i < height?.length) {
//     pot = Math.min(leftArr[i], rightArr[i]);
//     result += Math.max(0, pot - height[i]);
//     i++;
//   }

//   console.log(result);
// }
// console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));

function trap(height) {
  let left = 0;
  let right = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let result = 0;

  while (left <= right) {
    if (height[left] <= height[right]) {
      if (height[left] >= leftMax) {
        leftMax = height[left];
      } else {
        result += leftMax - height[left];
      }
      left++;
    } else {
      if (height[right] >= rightMax) {
        rightMax = height[right];
      } else {
        result += rightMax - height[right];
      }
      right--;
    }
  }
  return result;
}

console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
