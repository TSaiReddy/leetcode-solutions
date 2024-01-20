function merge(arr1, arr2) {
  let i = 0;
  let j = 0;
  let result = [];
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    }
    if (arr1[i] > arr2[j]) {
      result.push(arr2[j]);
      j++;
    }
    if (arr1[i] === arr2[j]) {
      result.push(arr1[i]);
      result.push(arr2[j]);
      i++;
      j++;
    }
  }
  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
}

function findMedianSortedArrays(nums1, nums2) {
  const result = merge(nums1, nums2);

  const len = result.length;
  const mid = Math.floor(len / 2);
  if (len % 2 === 0) {
    return (result[mid - 1] + result[mid]) / 2;
  } else {
    return result[mid];
  }
}

console.log(findMedianSortedArrays([], [-3, -2, -1, 1, 5]));
