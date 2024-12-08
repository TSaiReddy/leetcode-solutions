function largestSubArr(arr, k) {
  let subSum = arr.slice(0, k).reduce((acc, cur) => acc + cur, 0);
  let maxSum = subSum;

  for (let j = k; j < arr.length; j++) {
    subSum += arr[j] - arr[j - k];
    maxSum = Math.max(maxSum, subSum);
  }

  return maxSum;
}

console.log(largestSubArr([1, 2, 3, 4, 5, 6], 2));
console.log(largestSubArr([1, 2, 3, 7, 5, 6], 2));
